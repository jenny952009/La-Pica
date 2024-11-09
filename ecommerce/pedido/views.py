from django.shortcuts import render, redirect
from django.http import JsonResponse
from carrito.models import CarritoItem
from .forms import PedidoForm
import datetime
from .models import Pedido, Pago, PedidoProducto
import json
from tienda.models import Producto
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse



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

# Create your views here.
# Función para realizar el pedido
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
    # Calcular el total y la cantidad del carrito
    for carrito_item in carrito_items:
        total += (carrito_item.producto.precio * carrito_item.cantidad)
        cantidad += carrito_item.cantidad

    impuesto = round((19/100) * total, 2)
    gran_total = total 

    # Procesar el formulario de pedido si la solicitud es un POST
    if request.method == 'POST':
        form = PedidoForm(request.POST)

        if form.is_valid():            # Crea un nuevo pedido con los datos del formulario
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
            yr=int(datetime.date.today().strftime('%Y'))
            mt=int(datetime.date.today().strftime('%m'))
            dt=int(datetime.date.today().strftime('%d'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")
            pedido_numero = current_date + str(data.id)
            data.pedido_numero = pedido_numero
            data.save()
           
            # Obtiene el pedido para enviarlo a la página de pago
            pedido = Pedido.objects.get(user=actual_usuario, is_ordered=False, pedido_numero=pedido_numero)
        # Contexto para el template de pago
            context = {
                'pedido': pedido,
                'carrito_items': carrito_items,
                'total': total,
                'impuesto': impuesto,
                'gran_total': gran_total,
            }
            # Redirigir al pago
            return render(request, 'pedido/pago.html', context)
    
    # Si no es un método POST, redirigir a la página de checkout
    messages.info(request, 'Por favor, complete los datos de envío.')
    return redirect('checkout')     
   
# Función para mostrar el pedido completo después de la confirmación de compra
def pedido_completo(request):
    pedido_numero = request.GET.get('pedido_numero')
    transID = request.GET.get('pago_id')

    try:        # Obtener el pedido y los productos ordenados para mostrarlos en la página de confirmación
        pedido = Pedido.objects.get(pedido_numero=pedido_numero, is_ordered=True)
        ordered_products = PedidoProducto.objects.filter(pedido_id=pedido.id)

        subtotal = 0
        for i in ordered_products:
            subtotal += i.producto_precio*i.cantidad
      
        # Obtener el pago relacionado al pedido
        pago = Pago.objects.get(pago_id=transID)

                  
     # Contexto para la plantilla 
        context = {
            'pedido': pedido,
            'ordered_products':ordered_products,  # Ahora contiene enlaces de reseña,
            'pedido_numero': pedido.pedido_numero,
            'transID': pago.pago_id,
            'pago': pago,
            'subtotal': subtotal,
        }
          
        return render(request, 'pedido/pedido_completo.html', context)

    except(Pago.DoesNotExist, Pedido.DoesNotExist):
                # En caso de error, redirigir a la página de inicio
        messages.error(request, 'Hubo un problema con tu pedido. Inténtalo de nuevo.')
        return redirect('home')
    
    
        
