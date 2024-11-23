from django.db import models
from tienda.models import Producto  #, Variacion
from cuenta.models import Cuenta


class Carrito(models.Model):
    carrito_id = models.CharField(max_length=250, blank=True, verbose_name="Carrito" )
    fecha_agregado = models.DateField(auto_now_add=True, verbose_name="Fecha Agregado")

    def __str__(self):
        return self.carrito_id


class CarritoItem(models.Model):
    user = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=True, verbose_name="Usuario")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    carro = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True, verbose_name="Carro")
    cantidad = models.IntegerField(verbose_name="Cantidad de Producto")  # Aquí se agrega verbose_name
    is_active = models.BooleanField(default=True, verbose_name="¿Está Activo?")

    def sub_total(self):
        return self.producto.precio * self.cantidad

   
    def __unicode__(self):
        return self.producto


