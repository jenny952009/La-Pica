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
    rating = models.FloatField()  # Calificación del producto (1-5)
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
    
    
"""
#codigo antiguo:  

    def get_url(self):
        return reverse('producto_detalle', args=[self.categoria.slug, self.slug])

    def __str__(self):
        return self.producto_nombre
        
    def averageReview(self):
        reviews = RevisarRating.objects.filter(producto=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg


    def countRevisar(self):
        reviews = RevisarRating.objects.filter(producto=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
        
        
        
----------------------------------------------------------------------
class Variacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    variacion_categoria = models.CharField(max_length=100, choices=variacion_categoria_elegir) #variation_category_choice
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariacionGerente()


    def __str__(self):
        return self.variacion_categoria + ' : ' + self.variation_value
"""
""""
class VariacionGerente(models.Manager):
    def sabores(self):
        return super(VariacionGerente, self).filter(variacion_categoria='sabor', is_active=True)

    def tamaño(self):
        return super(VariacionGerente, self).filter(variacion_categoria='tamaño', is_active=True)


variacion_categoria_elegir = (
    ('sabor', 'sabor'),
    ('tamaño', 'tamaño'),
)
"""
"""
 def averageReview(self):
        
        reviews = ReseñaRating.objects.filter(producto=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

#Cuenta las reseñas activas (status=True) de un producto.
    def countReseña(self):
        reviews = ReseñaRating.objects.filter(producto=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count


class ReseñaRating(models.Model):
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    user = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, blank=True)#Título o asunto de la reseña
    #subject = models.CharField(max_length=100, blank=True)#Título o asunto de la reseña
    reseña = models.CharField(max_length=500, blank=True)# Comentario detallado de la reseña
    #review = models.CharField(max_length=500, blank=True)
    rating = models.FloatField()# Calificación del producto (1-5)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
"""