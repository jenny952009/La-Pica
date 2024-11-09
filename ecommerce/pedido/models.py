from django.db import models
from cuenta.models import Cuenta
from tienda.models import Producto 


# Create your models here.
class Pago(models.Model):
    user = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    pago_id = models.CharField(max_length=100)
    pago_method = models.CharField(max_length=100)
    monto_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pago_id


class Pedido(models.Model):
    STATUS = (
        ('New', 'Nuevo'),
        ('Accepted', 'Aceptado'),
        ('Completed', 'Completado'),
        ('Cancelled', 'Cancelado'),
    )


    user = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, null=True)
    pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, blank=True, null=True)
    pedido_numero = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    direccion_1 = models.CharField(max_length=100)
    direccion_2 = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)  # Agregado mio
    ciudad = models.CharField(max_length=50)  # Agregado mio
    region = models.CharField(max_length=20)  #
    pedido_nota = models.CharField(max_length=100, blank=True)
    pedido_total = models.FloatField()
    impuesto = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'


    def direccion_completa(self):
        return f'{self.direccion_1} {self.direccion_2}'


    def __str__(self):
        return self.nombre


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    producto_precio = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto.producto_nombre
