from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, RevisarRating, ProductoGaleria
from categoria.models import Categoria
from carrito.models import CarritoItem
from carrito.views import _carrito_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .forms import RevisarForm
from django.contrib import messages
from pedido.models import PedidoProducto

#from django.shortcuts import render


# Create your views here.
def tienda(request, category_slug=None):
    categorias = None
    productos = None

    if category_slug != None:
        categorias = get_object_or_404(Categoria, slug=category_slug)
        productos = Producto.objects.filter(categoria=categorias, is_available=True).order_by('id')
        paginator = Paginator(productos, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        producto_count = productos.count()
    else:
        productos = Producto.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(productos, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        producto_count = productos.count()


    context = {
        'productos' : paged_products,
        'producto_count' : producto_count,
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


    reviews = RevisarRating.objects.filter(producto__id=single_product.id, status=True)

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
    
    
    
    
def submit_review(request, producto_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = RevisarRating.objects.get(user__id=request.user.id, producto__id=producto_id)
            form = RevisarForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Muchas gracias!, tu comentario ha sido actualizado.')
            return redirect(url)
        except RevisarRating.DoesNotExist:
            form = RevisarForm(request.POST)
            if form.is_valid():
                data = RevisarRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.producto_id = producto_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Tu comentario ha sido publicado ¡Muchas gracias! .')
                return redirect(url)
