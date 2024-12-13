from django.db.models import Sum, Count
from django.db.models.functions import TruncDay, TruncMonth
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.utils import timezone
from pedido.models import Pedido, PedidoProducto
from .forms import FiltroVentasForm  # Asegúrate de que este formulario esté definido correctamente
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
import json

# Python imports
import datetime  # Para usar métodos como datetime.datetime y datetime.date
from datetime import time  # Para funciones específicas como time.min y time.max
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

#------------graficos--------------------------------    
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from .forms import FiltroVentasForm
from .models import Pedido, PedidoProducto, Producto
from django.utils.timezone import make_aware
from django.utils import timezone
from collections import Counter


@staff_member_required
def dashboard_ventas(request):
    # Inicializar el formulario de filtro
    form = FiltroVentasForm(request.GET or None)
    pedidos = Pedido.objects.all()

     # Aplicar filtros si el formulario es válido
    if form.is_valid():
        if form.cleaned_data.get('fecha_inicio'):
            pedidos = pedidos.filter(created_at__gte=form.cleaned_data['fecha_inicio'])
        if form.cleaned_data.get('fecha_fin'):
            pedidos = pedidos.filter(created_at__lte=form.cleaned_data['fecha_fin'])
        #if form.cleaned_data.get('estado'):
        #    pedidos = pedidos.filter(status=form.cleaned_data['estado'])
        # Filtrar por estado
        estado = form.cleaned_data.get('estado')
        if estado and estado != 'None':
            pedidos = pedidos.filter(status=estado)
            
        
    # Obtener la fecha de hoy con la zona horaria correcta
    today = timezone.localdate()  # Esto devuelve solo la fecha sin la hora
    #today_start = timezone.make_aware(datetime.combine(today, datetime.min.time()))  # Inicio de hoy
    #today_end = timezone.make_aware(datetime.combine(today, datetime.max.time()))  # Fin de hoy
    # Definir el inicio y fin de hoy
    today_start = make_aware(datetime.datetime.combine(today, datetime.time.min))  # Inicio de hoy
    today_end = make_aware(datetime.datetime.combine(today, datetime.time.max))  # Fin de hoy

    # 1. Pedidos nuevos (compras en línea)
    nuevos_pedidos = Pedido.objects.filter(created_at__gte=today_start, created_at__lte=today_end)
    total_nuevos_pedidos = nuevos_pedidos.count()

    # 2. Total de pedidos diarios
    total_ventas_diarias = nuevos_pedidos.aggregate(Sum('pedido_total'))['pedido_total__sum'] or 0
    total_ventas_diarias = int(total_ventas_diarias)
    # 3. Total del mes en ventas
    # Obtener el primer día del mes actual
    #hoy = timezone.localdate()  # Fecha de hoy
    primer_dia_mes = today.replace(day=1)  # Primer día del mes actual
    
    # Obtener las ventas del mes actual
    ventas_mes_actual = pedidos.filter(created_at__gte=primer_dia_mes).aggregate(total_ventas=Sum('pedido_total'))
    # Extraer el total de ventas del mes actual
    total_ventas_mes = int(ventas_mes_actual['total_ventas'] or 0)  # Si no hay ventas, poner 0
    
    
        # Gráfico 1: Ventas por estado
    
    estados = pedidos.values('status').annotate(total=Count('id')).order_by('status')

    # Gráfico 2: Productos más vendidos
    productos = PedidoProducto.objects.filter(pedido__in=pedidos) \
        .values('producto__producto_nombre') \
        .annotate(total=Sum('cantidad')) \
        .order_by('-total')[:5]
    
    # Gráfico 3: Ventas por mes (sin usar TruncMonth, lo haremos en Python)
    ventas_mes = pedidos.values('created_at').annotate(total=Sum('pedido_total')).order_by('created_at')

    # Convertir las fechas a meses (en vez de usar TruncMonth)
    ventas_mes_agrupadas = {}
    for venta in ventas_mes:
        # Convertir a un objeto datetime sin zona horaria (si aplica)
        fecha_venta = venta['created_at'].date()
        mes_anno = fecha_venta.strftime('%b %Y')
        if mes_anno in ventas_mes_agrupadas:
            ventas_mes_agrupadas[mes_anno] += venta['total']
        else:
            ventas_mes_agrupadas[mes_anno] = venta['total']

    # Ordenar por mes y año
    labels_ventas_mes = list(ventas_mes_agrupadas.keys())
    data_ventas_mes = list(ventas_mes_agrupadas.values())
    
    # Gráfico 4: Ventas por Categoría (asumimos que Producto tiene una relación con Categoría)
    ventas_por_categoria = PedidoProducto.objects.filter(pedido__in=pedidos) \
        .values('producto__categoria__categoria_nombre') \
        .annotate(total=Sum('cantidad')) \
        .order_by('-total')

    labels_ventas_categoria = [venta['producto__categoria__categoria_nombre'] for venta in ventas_por_categoria]
    data_ventas_categoria = [venta['total'] for venta in ventas_por_categoria]

    # Gráfico 5: Stock de productos (integración con app tienda)
    productos_stock = Producto.objects.all()
    labels_stock = [producto.producto_nombre for producto in productos_stock]
    data_stock = [producto.stock for producto in productos_stock]
 
    # Preparar el contexto para renderizar
    context = {
        'form': form,
        # Datos para el gráfico de ventas por estado
        'labels_estados': [status['status'] for status in estados],
        'data_estados': [status['total'] for status in estados],
        # Datos para el gráfico de productos más vendidos
        'labels_productos': [producto['producto__producto_nombre'] for producto in productos],
        'data_productos': [producto['total'] for producto in productos],
        # Datos para el gráfico de ventas por mes
        'labels_ventas_mes': labels_ventas_mes,
        'data_ventas_mes': data_ventas_mes,
        # Datos para el gráfico de ventas por categoría
        'labels_ventas_categoria': labels_ventas_categoria,
        'data_ventas_categoria': data_ventas_categoria,
       
        'total_nuevos_pedidos': total_nuevos_pedidos,
        'total_ventas_diarias': total_ventas_diarias,
        'total_ventas_mes': total_ventas_mes,
        'labels_stock': labels_stock,
        'data_stock': data_stock,
    }

    return render(request, 'dashboard_ventas.html', context)

