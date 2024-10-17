from .models import Carrito, CarritoItem
from .views import _carrito_id


def counter(request):
    carrito_count = 0

    try:
        carro = Carrito.objects.filter(carrito_id=_carrito_id(request))

        if request.user.is_authenticated:
            carrito_items = CarritoItem.objects.all().filter(user=request.user)
        else:
            carrito_items = CarritoItem.objects.all().filter(carro=carro[:1])

        for carrito_item in carrito_items:
            carrito_count += carrito_item.cantidad
    except Carrito.DoesNotExist:
        carrito_count = 0
    return dict(carrito_count=carrito_count)
