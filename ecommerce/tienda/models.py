from django.db import models
from categoria.models import Categoria
from django.urls import reverse
from cuenta.models import Cuenta
from django.db.models import Avg, Count


# Create your models here.
class Producto(models.Model):
    producto_nombre = models.CharField(
        max_length=200, 
        unique=True, 
        verbose_name="Nombre del producto"
    )
    slug = models.CharField(
        max_length=200, 
        unique=True, 
        verbose_name="Slug"
    )
    descripcion = models.TextField(
        max_length=500, 
        blank=True, 
        verbose_name="Descripción"
    )
    precio = models.IntegerField(
        verbose_name="Precio"
    )
    images = models.ImageField(
        upload_to='fotos/productos', 
        verbose_name="Imagen del producto"
    )
    stock = models.IntegerField(
        verbose_name="Stock"
    )
    is_available = models.BooleanField(
        default=True, 
        verbose_name="Disponible"
    )
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        verbose_name="Categoría"
    )
    created_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Fecha de creación"
    )
    modified_date = models.DateTimeField(
        auto_now=True, 
        verbose_name="Fecha de modificación"
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-created_date']


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
""""
class ReseñaRating(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name=)
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
"""

class ReseñaRating(models.Model):
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        verbose_name="Producto"
    )
    user = models.ForeignKey(
        Cuenta, 
        on_delete=models.CASCADE, 
        verbose_name="Usuario"
    )
    titulo = models.CharField(
        max_length=100, 
        blank=True, 
        verbose_name="Título"
    )
    reseña = models.CharField(
        max_length=500, 
        blank=True, 
        verbose_name="Reseña"
    )
    rating = models.FloatField(
        verbose_name="Calificación Reseña"
    )  
    ip = models.CharField(
        max_length=20, 
        blank=True, 
        verbose_name="Dirección IP"
    )
    status = models.BooleanField(
        default=True, 
        verbose_name="Estado"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Creado el"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Actualizado el"
    )

    class Meta:
        verbose_name = "Reseña y calificación"
        verbose_name_plural = "Reseñas y calificaciones"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.producto} - {self.titulo or 'Sin título'} ({self.rating})"
""""    
class ProductoGaleria(models.Model):
    producto = models.ForeignKey(Producto, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tienda/productos', max_length=255)
"""
class ProductoGaleria(models.Model):
    producto = models.ForeignKey(
        Producto, 
        default=None, 
        on_delete=models.CASCADE, 
        verbose_name="Producto"
    )
    image = models.ImageField(
        upload_to='tienda/productos', 
        max_length=255, 
        verbose_name="Imagen"
    )

    class Meta:
        verbose_name = "Galería de producto"
        verbose_name_plural = "Galerías de productos"
        ordering = ['producto']

    def __str__(self):
        return f"Imagen de {self.producto.producto_nombre}"

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