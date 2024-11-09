from django.shortcuts import render
from tienda.models import Producto, ReseñaRating

def home(request):
    productos = Producto.objects.all().filter(is_available=True).order_by('created_date')

    # Inicializar 'reviews' como lista vacía fuera del bucle
    reviews = []
    for producto in productos:
        producto_reviews = ReseñaRating.objects.filter(producto_id=producto.id, status=True)
        reviews.extend(producto_reviews)  # Agregar las reseñas de cada producto a la lista 'reviews'

    context = {
        'productos': productos,
        'reviews': reviews,  # Aquí estarán todas las reseñas de todos los productos
    }

    return render(request, 'home.html', context)
