from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, ReseñaRating, ProductoGaleria
from categoria.models import Categoria
from carrito.models import Carrito, CarritoItem
from carrito.views import _carrito_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .forms import ReseñaForm
from django.contrib import messages
from pedido.models import PedidoProducto
from django.urls import reverse
from django.http import JsonResponse  # Import necesario para devolver JSON


def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    cantidad = 1  # Incremento por defecto
    carrito_item = CarritoItem.objects.filter(carro__carrito_id=_carrito_id(request), producto=producto).first()

    if carrito_item:
        if carrito_item.cantidad + cantidad > producto.stock:
            messages.error(request, "No puedes agregar más productos de los disponibles en el stock.")
        else:
            carrito_item.cantidad += cantidad
            carrito_item.save()
    else:
        if cantidad > producto.stock:
            messages.error(request, "La cantidad excede el stock disponible.")
        else:
            carrito = Carrito.objects.get_or_create(carrito_id=_carrito_id(request))[0]
            CarritoItem.objects.create(
                producto=producto,
                carro=carrito,
                cantidad=cantidad
            )

    return redirect('ver_carrito')  # Cambia esto por el nombre de tu URL para el carrito

# Otras vistas existentes
def tienda(request, category_slug=None):
    categorias = None
    productos = None

    if category_slug is not None:
        categorias = get_object_or_404(Categoria, slug=category_slug)
        productos = Producto.objects.filter(categoria=categorias, is_available=True, stock__gt=0).order_by('id')
    else:
        productos = Producto.objects.filter(is_available=True, stock__gt=0).order_by('id')
    
    paginator = Paginator(productos, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    producto_count = productos.count()

    context = {
        'productos': paged_products,
        'producto_count': producto_count,
    }

    return render(request, 'tienda/tienda.html', context)

def producto_detalle(request, category_slug, product_slug):
    try:
        single_product = Producto.objects.get(categoria__slug=category_slug, slug=product_slug)
        in_cart = CarritoItem.objects.filter(carro__carrito_id=_carrito_id(request), producto=single_product).exists()
    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            pedidoproducto = PedidoProducto.objects.filter(user=request.user, producto__id=single_product.id).exists()
        except PedidoProducto.DoesNotExist:
            pedidoproducto = None
    else:
        pedidoproducto = None

    reviews = ReseñaRating.objects.filter(producto__id=single_product.id, status=True)

    producto_galeria = ProductoGaleria.objects.filter(producto_id=single_product.id)

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'pedidoproducto': pedidoproducto,
        'reviews': reviews,
        'producto_galeria': producto_galeria,
    }

    return render(request, 'tienda/producto_detalle.html', context)

def search(request):
    productos = []  # Inicializa la lista vacía
    producto_count = 0  # Inicializa el conteo

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            productos = Producto.objects.order_by('-created_date').filter(
                Q(descripcion__icontains=keyword) | Q(producto_nombre__icontains=keyword)
            )
            producto_count = productos.count()

    context = {
        'productos': productos,
        'producto_count': producto_count,
    }

    return render(request, 'tienda/tienda.html', context)


def actualizar_productos(request, category_slug=None):
    if category_slug:
        categoria = get_object_or_404(Categoria, slug=category_slug)
        productos = Producto.objects.filter(categoria=categoria, is_available=True, stock__gt=0).order_by('id')
    else:
        productos = Producto.objects.filter(is_available=True, stock__gt=0).order_by('id')

    # Paginación de productos
    paginator = Paginator(productos, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    # Si es una solicitud AJAX, solo devolveremos los productos (HTML parcial)
    if request.is_ajax():
        return render(request, 'tienda/productos_partial.html', {'productos': paged_products})
    
    # Si no es AJAX, simplemente devolver la respuesta normal
    productos_data = [
        {
            'nombre': producto.producto_nombre,
            'precio': producto.precio,
            'stock': producto.stock,
            'imagen': producto.images.url if producto.images else '',
        }
        for producto in productos
    ]

    return JsonResponse({'success': True, 'productos': productos_data})



    
    
    
    
#-----------------------------comentarios-------------------------------------------    
# Vista para enviar una reseña  
def agregar_reseña(request, producto_id):
    # Recupera la URL de referencia o usa una URL predeterminada si no existe
    url = request.META.get('HTTP_REFERER')  # Guarda la URL previa para redirigir después del procesamiento de la reseña

    # Verifica si la solicitud es POST (es decir, si el formulario fue enviado)
    if request.method == 'POST':
        form = ReseñaForm(request.POST)

        # Verifica que el formulario es válido
        if form.is_valid():
            # Verifica que el campo `rating` no esté vacío
            rating = form.cleaned_data.get('rating')
            titulo = form.cleaned_data.get('titulo')
            reseña = form.cleaned_data.get('reseña')

            if rating and titulo and reseña:  # Asegúrate de que todos los campos estén completos
                data = ReseñaRating()  # Guarda la reseña
                data.titulo = titulo
                data.rating = rating
                data.reseña = reseña
                data.ip = request.META.get('REMOTE_ADDR')
                data.producto = get_object_or_404(Producto, id=producto_id)  # Obtén el producto
                data.user = request.user
                data.save()

                # Mensaje de éxito
                messages.success(request, 'Tu comentario ha sido publicado. ¡Gracias!')
            else:
                # Mensaje de error si faltan campos
                messages.error(request, 'Por favor, completa todos los campos antes de enviar.')
        else:
            messages.error(request, 'El formulario contiene errores. Por favor, verifica los datos ingresados.')

        # Redirige a la página previa o a la página de detalle del producto
        return redirect(url if url else reverse('producto_detalle', args=[producto_id]))

    return redirect('home')  # Redirigir al home
