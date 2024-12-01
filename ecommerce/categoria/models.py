from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    categoria_nombre = models.CharField(max_length=20, unique=True, verbose_name="Categoria")
    descripcion = models.CharField(max_length=255, blank=True, verbose_name="Descripción")
    slug =  models.CharField(max_length=100, unique=True, verbose_name="Slug")
    cat_image =  models.ImageField(upload_to='photos/categorias', blank=True, verbose_name="Imagen Categoría")

    class Meta:
        verbose_name = 'Categoria'     # Nombre en singular
        verbose_name_plural = 'Categorias' # Nombre en plural

    # Método que genera la URL para acceder a los productos de esta categoría.
    def get_url(self):
        return reverse('productos_por_categoria', args=[self.slug])

    # Representación en cadena del objeto
    def __str__(self):
        
        return self.categoria_nombre # Retorna el nombre de la categoría 
