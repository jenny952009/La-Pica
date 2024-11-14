from django.db import models
from tienda.models import Producto  #, Variacion
from cuenta.models import Cuenta


class Carrito(models.Model):
    carrito_id = models.CharField(max_length=250, blank=True)
    fecha_agregado = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.carrito_id


class CarritoItem(models.Model):
    user = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.producto.precio * self.cantidad

   
    def __unicode__(self):
        return self.producto


