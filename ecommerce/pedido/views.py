from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Sum

from carrito.models import CarritoItem
from tienda.models import Producto
from .models import Pedido, Pago, PedidoProducto
from .forms import PedidoForm, FiltroVentasForm

import datetime
import json

def pago(request):    # Carga los datos enviados en la solicitud POST
    try:
        body = json.loads(request.body)
        # Obtiene el pedido no confirmado para el usuario actual según el pedidoID recibido
        pedido = Pedido.objects.get(user=request.user, is_ordered=False, pedido_numero=body['pedidoID'])
        # Crea un nuevo registro de pago usando los datos recibidos
        pago = Pago(
            user = request.user,
            pago_id = body['transID'],
            pago_method = body['pago_method'],
            monto_id = pedido.pedido_total,
            status = body['status'],
        )

        pago.save()
        # Actualiza el pedido con el pago realizado y lo marca como "ordenado"
        pedido.pago = pago
        pedido.is_ordered = True
        pedido.save()
        # Obtiene todos los elementos del carrito del usuario actual
        carrito_items = CarritoItem.objects.filter(user=request.user)
        # Procesa cada elemento en el carrito y crea un registro de PedidoProducto
        for item in carrito_items:
            pedidoproducto = PedidoProducto()
            pedidoproducto.pedido_id = pedido.id
            pedidoproducto.pago = pago
            pedidoproducto.user_id = request.user.id
            pedidoproducto.producto_id = item.producto_id
            pedidoproducto.cantidad = item.cantidad
            pedidoproducto.producto_precio = item.producto.precio
            pedidoproducto.ordered = True
            pedidoproducto.save()
            
            # Actualiza el stock del producto en base a la cantidad comprada
            producto = Producto.objects.get(id=item.producto_id)
            producto.stock -= item.cantidad

            # Sumar la cantidad comprada a la columna Ventas
            producto.ventas += item.cantidad
            producto.save()

        # Vacía el carrito del usuario después de confirmar el pedido
        CarritoItem.objects.filter(user=request.user).delete()

        # Envío de correo electrónico de confirmación de compra
        mail_subject = 'Tu compra fue realizada!'
        body = render_to_string('pedido/pedido_recibido_email.html', {
            'user': request.user,
            'pedido': pedido,
        })

        to_email = request.user.email
        try:
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()

        except Exception as e:
            print(f"Error al enviar el correo: {e}")

        # Respuesta JSON con detalles del pedido y transacción
        data = {
            'pedido_numero': pedido.pedido_numero,
            'transID': pago.pago_id,
        }

        return JsonResponse(data)

    except Pedido.DoesNotExist:
        return JsonResponse({'error': 'Pedido no encontrado.'}, status=404)

#funcion del formulario de direccion de envio con sus campos a rellenar y vista de la pagina checkout

def place_order(request, total=0, cantidad=0):
    actual_usuario = request.user
    carrito_items = CarritoItem.objects.filter(user=actual_usuario)
    carrito_count = carrito_items.count()
    
    # Si el carrito está vacío, redirigir a la tienda
    if carrito_count <= 0:
        return redirect('tienda')
    
    # Calcula el total y el impuesto para los elementos en el carrito
    gran_total = 0
    impuesto = 0

    # Calcular el total y la cantidad de productos
    for carrito_item in carrito_items:
        total += (carrito_item.producto.precio * carrito_item.cantidad)
        cantidad += carrito_item.cantidad

    impuesto = round((19 / 100) * total, 2)
    gran_total = total + impuesto  # Incluye el IVA en el total

# formateado como un número entero sin decimales
    gran_total_formatted = "{:.0f}".format(gran_total)  # Convertir a string sin decimales
    
    # Procesar el formulario de pedido si la solicitud es un POST
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            # Crear un nuevo pedido con los datos del formulario
            data = Pedido()
            data.user = actual_usuario
            data.nombre = form.cleaned_data['nombre']
            data.apellido = form.cleaned_data['apellido']
            data.telefono = form.cleaned_data['telefono']
            data.email = form.cleaned_data['email']
            data.direccion_1 = form.cleaned_data['direccion_1']
            data.direccion_2 = form.cleaned_data['direccion_2']
            data.pais = form.cleaned_data['pais']
            data.ciudad = form.cleaned_data['ciudad']
            data.region = form.cleaned_data['region']
            data.pedido_nota = form.cleaned_data['pedido_nota']
            data.pedido_total = gran_total
            data.impuesto = impuesto
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # Crear un número de pedido único basado en la fecha y el ID del pedido
            yr = int(datetime.date.today().strftime('%Y'))
            mt = int(datetime.date.today().strftime('%m'))
            dt = int(datetime.date.today().strftime('%d'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            pedido_numero = current_date + str(data.id)
            data.pedido_numero = pedido_numero
            data.save()

            # Obtener el pedido y pasar al proceso de pago
            pedido = Pedido.objects.get(user=actual_usuario, is_ordered=False, pedido_numero=pedido_numero)
            
            # Contexto para el template de pago
            context = {
                'pedido': pedido,
                'carrito_items': carrito_items,
                'total': total,
                'impuesto': impuesto,
                'gran_total': gran_total,
                'gran_total_formatted': gran_total_formatted,  # Pasamos el total sin decimales

            }
            # Redirigir al pago
            return render(request, 'pedido/pago.html', context)
        else:
            # Si el formulario no es válido, se mantiene en la página de checkout
            context = {
                'form': form,
                'carrito_items': carrito_items,
                'total': total,
                'impuesto': impuesto,
                'gran_total': gran_total,
            }
            return render(request, 'tienda/checkout.html', context)

    else:
        form = PedidoForm()

    # Si la solicitud es GET, mostramos el formulario vacío en la página de checkout
    context = {
        'form': form,
        'carrito_items': carrito_items,
        'total': total,
        'impuesto': impuesto,
        'gran_total': gran_total,
        
    }
    return render(request, 'tienda/checkout.html', context)
    
    # Si no es un método POST, redirigir a la página de checkout
    #messages.info(request, 'Por favor, complete los datos de envío.')
    return redirect('checkout')     
   
# Función para mostrar el pedido completo después de la confirmación de compra

def pedido_completo(request):
    pedido_numero = request.GET.get('pedido_numero')
    transID = request.GET.get('pago_id')

    try:
        # Obtener el pedido y los productos ordenados para mostrarlos en la página de confirmación
        pedido = Pedido.objects.get(pedido_numero=pedido_numero, is_ordered=True)
        ordered_products = PedidoProducto.objects.filter(pedido_id=pedido.id)

        subtotal = 0
        # Crear una lista de productos con el total calculado (precio * cantidad)
        for i in ordered_products:
            i.total_producto = i.producto_precio * i.cantidad  # Agregar el total del producto
            subtotal += i.total_producto  # Sumar el total de cada producto al subtotal

        # Obtener el pago relacionado al pedido
        pago = Pago.objects.get(pago_id=transID)

        # Calcular el total (incluyendo impuestos, si los hay)
        total = subtotal + pedido.impuesto  # Asegúrate de que pedido.impuesto está correctamente asignado

        # Contexto para la plantilla
        context = {
            'pedido': pedido,
            'ordered_products': ordered_products,  # Ahora contiene el total de cada producto
            'pedido_numero': pedido.pedido_numero,
            'transID': pago.pago_id,
            'pago': pago,
            'subtotal': subtotal,
            'total': total,  # Total con impuestos
        }
          
        return render(request, 'pedido/pedido_completo.html', context)

    except(Pago.DoesNotExist, Pedido.DoesNotExist):
        # En caso de error, redirigir a la página de inicio
        messages.error(request, 'Hubo un problema con tu pedido. Inténtalo de nuevo.')
        return redirect('home')

#----------------------------------------------------
# Dashboard de ventas
@staff_member_required
def dashboard_ventas(request):
    # Inicializar el formulario de filtro
    form = FiltroVentasForm(request.GET or None)
    pedidos = Pedido.objects.all()
            
    # Aplicar filtros si el formulario es válido
    if form.is_valid():
        if form.cleaned_data.get('created_at'):
            pedidos = pedidos.filter(fecha__gte=form.cleaned_data['created_at'])
        if form.cleaned_data.get('created_at'):
            pedidos = pedidos.filter(fecha__lte=form.cleaned_data['created_at'])
        if form.cleaned_data.get('status'):
            pedidos = pedidos.filter(status=form.cleaned_data['status'])

    # Filtrar por estado, pero solo si se selecciona un estado
        estado_seleccionado = form.cleaned_data.get('estado')
        if estado_seleccionado and estado_seleccionado != '':
            pedidos = pedidos.filter(status=estado_seleccionado)

    # Generar datos para los gráficos
    estados = pedidos.values('status').annotate(total=Count('id')).order_by('status')
        
    #productos = pedidos.values('producto__nombre').annotate(total=Sum('cantidad')).order_by('-total')[:5]
    productos = PedidoProducto.objects.filter(pedido__in=pedidos) \
        .values('producto__producto_nombre') \
        .annotate(total=Sum('cantidad')) \
        .order_by('-total')[:5]
        
    context = {
        'form': form,
        # Datos para el gráfico de ventas por estado
        'labels_estados': [status['status'] for status in estados],
        'data_estados': [status['total'] for status in estados],
        # Datos para el gráfico de productos más vendidos
        'labels_productos': [producto['producto__producto_nombre'] for producto in productos],
        'data_productos': [producto['total'] for producto in productos],
    }
    return render(request, 'dashboard_ventas.html', context)
     
    
"""
@staff_member_required
def dashboard_ventas(request):
    # Ventas por Estado
    estados = Pedido.objects.values('status').annotate(total=Count('id')).order_by('status')
    labels_estados = [estado['status'] for estado in estados]
    data_estados = [estado['total'] for estado in estados]

    # Productos más vendidos
    productos_vendidos = PedidoProducto.objects.values('producto__producto_nombre') \
        .annotate(cantidad_vendida=Count('id')) \
        .order_by('-cantidad_vendida')[:10]  # Limitar a los 10 productos más vendidos
    labels_productos = [producto['producto__producto_nombre'] for producto in productos_vendidos]
    data_productos = [producto['cantidad_vendida'] for producto in productos_vendidos]

    context = {
        'labels_estados': labels_estados,
        'data_estados': data_estados,
        'labels_productos': labels_productos,
        'data_productos': data_productos,
    }

    return render(request, 'dashboard_ventas.html', context)

#-----------------
"""