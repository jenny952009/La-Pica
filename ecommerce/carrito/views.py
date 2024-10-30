from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Producto, Variacion
from .models import Carrito, CarritoItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


# Create your views here.
# Función para obtener el ID del carrito de la sesión
def _carrito_id(request):
    carro = request.session.session_key
    if not carro:
        carro = request.session.create()
    return carro

# Función para agregar un producto al carrito

def agregar_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)  # Obtiene el producto por ID

    actual_usuario = request.user  # Obtiene el usuario actual

    if actual_usuario.is_authenticated:
        # Usuario autenticado
        producto_variacion = []

        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try: # Busca la variación del producto según la categoría y el valor

                    variacion = Variacion.objects.get(producto=producto, variacion_categoria__iexact=key, variation_value__iexact=value)
                    producto_variacion.append(variacion)
                except:
                    pass
                
        # Verifica si el ítem del carrito ya existe
        is_cart_item_exists = CarritoItem.objects.filter(producto=producto, user=actual_usuario).exists()

        if is_cart_item_exists:
            carrito_item = CarritoItem.objects.filter(producto=producto, user=actual_usuario)

            ex_var_list = []
            id = []
            for item in carrito_item:
                existing_variation = item.variacion.all() # Obtiene las variaciones del ítem existente
                ex_var_list.append(list(existing_variation)) # Añade las variaciones a la lista
                id.append(item.id)
                
            # Si las variaciones del producto ya están en el carrito
            if producto_variacion in ex_var_list:
                index = ex_var_list.index(producto_variacion)
                item_id = id[index]
                item = CarritoItem.objects.get(producto=producto, id=item_id)
                item.cantidad += 1
                item.save()
            else:                 # Crea un nuevo ítem en el carrito si la variación no existe
                item = CarritoItem.objects.create(producto=producto, cantidad=1, user=actual_usuario)
                if len(producto_variacion) > 0:
                    item.variacion.clear()
                    item.variacion.add(*producto_variacion)
                item.save()

        else :
             # Si el ítem no existe
            # Crea un nuevo ítem en el carrito
            carrito_item = CarritoItem.objects.create(
                producto = producto,
                cantidad = 1,
                user = actual_usuario,
            )
            if len(producto_variacion) > 0:
                carrito_item.variacion.clear()
                carrito_item.variacion.add(*producto_variacion)
            carrito_item.save()

        return redirect('carro')

    else:
        producto_variacion = []

        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    variacion = Variacion.objects.get(producto=producto, variacion_categoria__iexact=key, variation_value__iexact=value)
                    producto_variacion.append(variacion)
                except:
                    pass

        try:        # Intenta obtener el carrito existente o crear uno nuevo
            carro = Carrito.objects.get(carrito_id=_carrito_id(request))
        except Carrito.DoesNotExist:
            carro = Carrito.objects.create(
                carrito_id = _carrito_id(request)
            )
        carro.save()

        # Verifica si el ítem del carrito ya existe
        is_cart_item_exists = CarritoItem.objects.filter(producto=producto, carro=carro).exists()
        if is_cart_item_exists:
            carrito_item = CarritoItem.objects.filter(producto=producto, carro=carro)

            ex_var_list = []
            id = []
            for item in carrito_item:
                existing_variation = item.variacion.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
          
            # Si las variaciones del producto ya están en el carrito
            if producto_variacion in ex_var_list:
                index = ex_var_list.index(producto_variacion)
                item_id = id[index]
                item = CarritoItem.objects.get(producto=producto, id=item_id)
                item.cantidad += 1
                item.save()
            else:                 # Crea un nuevo ítem en el carrito si la variación no existe
                item = CarritoItem.objects.create(producto=producto, cantidad=1, carro=carro)
                if len(producto_variacion) > 0:
                    item.variacion.clear()
                    item.variacion.add(*producto_variacion)
                item.save()

        # Normal nota
        else:
            carrito_item = CarritoItem.objects.create(
                producto = producto,
                cantidad = 1,
                carro = carro,
            )
            if len(producto_variacion) > 0:
                carrito_item.variacion.clear()
                carrito_item.variacion.add(*producto_variacion)
            carrito_item.save()

        return redirect('carro')

# Función para remover un ítem del carrito (reduce cantidad o elimina)
def remover_carrito(request, producto_id, carrito_item_id):
    producto = get_object_or_404(Producto, id= producto_id) # Obtiene el producto o devuelve 404

    try:
        if request.user.is_authenticated:
            carrito_item = CarritoItem.objects.get(producto= producto, user=request.user, id= carrito_item_id)
        else:
            carro = Carrito.objects.get(carrito_id=_carrito_id(request))
            carrito_item = CarritoItem.objects.get(producto=producto, carro=carro, id= carrito_item_id)
        # Reduce la cantidad del ítem o lo elimina si la cantidad es 1
        if carrito_item.cantidad > 1:
            carrito_item.cantidad -= 1
            carrito_item.save()
        else:
            carrito_item.delete() # Elimina el ítem del carrito
    except:
        pass

    return redirect('carro')

    # Remueve un item específico del carrito
def remover_carrito_item(request, producto_id, carrito_item_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.user.is_authenticated:
        carrito_item = CarritoItem.objects.get(producto=producto, user=request.user, id=carrito_item_id)
    else:
        carro = Carrito.objects.get(carrito_id=_carrito_id(request))
        carrito_item = CarritoItem.objects.get(producto=producto, carro=carro, id=carrito_item_id)

    carrito_item.delete()
    return redirect('carro')

    # Muestra el contenido del carrito
def carro(request, total=0, cantidad=0, carrito_items=None):
    impuesto = 0
    gran_total = 0
    try:
        if request.user.is_authenticated:
            carrito_items = CarritoItem.objects.filter(user=request.user, is_active=True)
        else:
            carro = Carrito.objects.get(carrito_id=_carrito_id(request))
            carrito_items = CarritoItem.objects.filter(carro=carro, is_active=True)

        for carrito_item in carrito_items:
            total += (carrito_item.producto.precio * carrito_item.cantidad)
            cantidad += carrito_item.cantidad
        impuesto = round((19/100) * total, 2)
        gran_total = total + impuesto

    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'cantidad': cantidad,
        'carrito_items': carrito_items,
        'impuesto': impuesto,
        'gran_total': gran_total,
    }


    return render(request, 'tienda/carro.html', context)

#Asegura que solo los usuarios autenticados puedan acceder a esta vista.
@login_required(login_url='login')
def checkout(request, total=0, cantidad=0, carrito_items=None):
    impuesto = 0
    gran_total = 0

    try:
        if request.user.is_authenticated:
            carrito_items = CarritoItem.objects.filter(user=request.user, is_active=True)
        else:
            carro = Carrito.objects.get(carrito_id=_carrito_id(request))
            carrito_items = CarritoItem.objects.filter(carro=carro, is_active=True)
       
        # Calcula el total y la cantidad de productos en el carrito.
        for carrito_item in carrito_items:
            total += (carrito_item.producto.precio * carrito_item.cantidad)
            cantidad += carrito_item.cantidad
        impuesto = round((19/100) * total, 2)
        gran_total = total + impuesto

    except ObjectDoesNotExist:
        pass
    # Contexto que se pasará a la plantilla de checkout.
    context = {
        'total': total,
        'cantidad': cantidad,
        'carrito_items': carrito_items,# Lista de elementos del carrito
        'impuesto': impuesto,
        'gran_total': gran_total,
    }

    # Renderiza la plantilla de checkout con el contexto
    return render(request, 'tienda/checkout.html', context)
