from django.shortcuts import render
from tienda.models import Producto, RevisarRating

def home(request):
    productos = Producto.objects.all().filter(is_available=True).order_by('created_date')

     # Diccionario para almacenar reseñas por producto
    reviews_dict = {}
    
    for producto in productos:
        reviews = RevisarRating.objects.filter(producto_id=producto.id, status=True)
        reviews_dict[producto.id] = reviews  # Almacenar reseñas en el diccionario

    context = {
        'productos': productos,
        'reviews_dict': reviews_dict, # Pasar el diccionario de reseñas
    }

    return render(request, 'home.html', context)
