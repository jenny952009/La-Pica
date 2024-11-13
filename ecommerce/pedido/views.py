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


def pago(request):
    body = json.loads(request.body)
    pedido = Pedido.objects.get(user=request.user, is_ordered=False, pedido_numero=body['pedidoID'])

    pago = Pago(
        user = request.user,
        pago_id = body['transID'],
        pago_method = body['pago_method'],
        monto_id = pedido.pedido_total,
        status = body['status'],
    )

    pago.save()
    pedido.pago = pago
    pedido.is_ordered = True
    pedido.save()

    carrito_items = CarritoItem.objects.filter(user=request.user)

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

        carrito_item = CarritoItem.objects.get(id=item.id)
        producto_variacion = carrito_item.variacion.all()
        pedidoproducto = PedidoProducto.objects.get(id=pedidoproducto.id)
        pedidoproducto.variacion.set(producto_variacion)
        pedidoproducto.save()

        producto = Producto.objects.get(id=item.producto_id)
        producto.stock -= item.cantidad
        producto.save()

    CarritoItem.objects.filter(user=request.user).delete()

    mail_subject = 'Tu compra fue realizada!'
    body = render_to_string('pedido/pedido_recibido_email.html', {
        'user': request.user,
        'pedido': pedido,
    })

    to_email = request.user.email
    send_email = EmailMessage(mail_subject, body, to=[to_email])
    send_email.send()

    data = {
        'pedido_numero': pedido.pedido_numero,
        'transID': pago.pago_id,
    }


    return JsonResponse(data)


#funcion del formulario de direccion de envio con sus campos a rellenar y vista de la pagina checkout
def place_order(request, total=0, cantidad=0):
    actual_usuario = request.user
    carrito_items = CarritoItem.objects.filter(user=actual_usuario)
    carrito_count = carrito_items.count()

    if carrito_count <= 0:
        return redirect('tienda')

    gran_total = 0
    impuesto = 0

    # Calcular el total y la cantidad de productos
    for carrito_item in carrito_items:
        total += (carrito_item.producto.precio * carrito_item.cantidad)
        cantidad += carrito_item.cantidad

    impuesto = round((19/100) * total, 2)
    gran_total = total + impuesto

    if request.method == 'POST':
        form = PedidoForm(request.POST)

        if form.is_valid():
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

            # Generación del número de pedido
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
            context = {
                'pedido': pedido,
                'carrito_items': carrito_items,
                'total': total,
                'impuesto': impuesto,
                'gran_total': gran_total,
            }

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


def pedido_completo(request):
    pedido_numero = request.GET.get('pedido_numero')
    transID = request.GET.get('pago_id')

    try:
        pedido = Pedido.objects.get(pedido_numero=pedido_numero, is_ordered=True)
        ordered_products = PedidoProducto.objects.filter(pedido_id=pedido.id)

        subtotal = 0
        for i in ordered_products:
            subtotal += i.producto_precio*i.cantidad

        pago = Pago.objects.get(pago_id=transID)

        context = {
            'pedido': pedido,
            'ordered_products': ordered_products,
            'pedido_numero': pedido.pedido_numero,
            'transID': pago.pago_id,
            'pago': pago,
            'subtotal': subtotal,
        }

        return render(request, 'pedido/pedido_completo.html', context)

    except(Pago.DoesNotExist, Pedido.DoesNotExist):
        return redirect('home')
