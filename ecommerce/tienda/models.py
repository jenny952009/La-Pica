from django.db import models
from categoria.models import Categoria
from django.urls import reverse
from cuenta.models import Cuenta
from django.db.models import Avg, Count


# Create your models here.
class Producto(models.Model):
    producto_nombre = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.IntegerField()
    images = models.ImageField(upload_to='fotos/productos')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('producto_detalle', args=[self.categoria.slug, self.slug])

    def __str__(self):
        return self.producto_nombre
      
   # Calcula el promedio de las reseñas de un producto
    def averageReview(self):
        reviews = ReseñaRating.objects.filter(producto=self, status=True).aggregate(average=Avg('rating'))
        return float(reviews['average']) if reviews['average'] is not None else 0.0

    # Cuenta las reseñas activas de un producto
    def countReseña(self):
        reviews = ReseñaRating.objects.filter(producto=self, status=True).aggregate(count=Count('id'))
        return int(reviews['count']) if reviews['count'] is not None else 0

class ReseñaRating(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    user = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, blank=True)
    reseña = models.CharField(max_length=500, blank=True)
    rating = models.FloatField()  
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class ProductoGaleria(models.Model):
    producto = models.ForeignKey(Producto, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tienda/productos', max_length=255)

    def __str__(self):
        return self.producto.producto_nombre
#Se agregra staticmethod
    @staticmethod
    def get_first_image(producto):
        galeria = ProductoGaleria.objects.filter(producto=producto).first()
        return galeria.image.url if galeria else 'path/to/default/image.png'
    
    def get_stars(self):
        """Devuelve el promedio de estrellas del producto asociado."""
        return self.producto.averageReview()
    get_stars.short_description = "Estrellas promedio" 
    
    def get_stars(self):
        """Devuelve el promedio de estrellas del producto asociado con 2 decimales."""
        average = self.producto.averageReview()
        return f"{average:.2f}"  # Formatea el promedio a 2 decimales
    get_stars.short_description = "Estrellas promedio"  # Nombre en el admin