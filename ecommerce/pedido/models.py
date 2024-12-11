from django.db import models
from cuenta.models import Cuenta
from tienda.models import Producto 


# Create your models here.
class Pago(models.Model):
    user = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name="Usuario")
    pago_id = models.CharField(max_length=100, verbose_name="ID de Pago")
    pago_method = models.CharField(max_length=100, verbose_name="Método de Pago")
    monto_id = models.CharField(max_length=100, verbose_name="Monto ID")
    status = models.CharField(max_length=100, verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.pago_id


class Pedido(models.Model):
    STATUS = (
        ('New', 'Nuevo'),
        ('Accepted', 'Aceptado'),
        ('Completed', 'Completado'),
        ('Cancelled', 'Cancelado'),
    )

    user = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, null=True, verbose_name="Usuario")
    pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Pago")
    pedido_numero = models.CharField(max_length=20, verbose_name="Número de Pedido")
    nombre = models.CharField(max_length=50, blank=False, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, blank=False, verbose_name="Apellido")
    telefono = models.CharField(max_length=50, blank=False, verbose_name="Teléfono")
    email = models.CharField(max_length=50, blank=False, verbose_name="Correo Electrónico")
    direccion_1 = models.CharField(max_length=100, blank=False, verbose_name="Dirección")
    direccion_2 = models.CharField(max_length=100, blank=True, verbose_name="Detalle Dirección (opcional)")
    pais = models.CharField(max_length=50, blank=False, verbose_name="País")
    ciudad = models.CharField(max_length=50, blank=False, verbose_name="Ciudad")
    region = models.CharField(max_length=20, blank=False, verbose_name="Región")
    pedido_nota = models.CharField(max_length=100, blank=True, verbose_name="Nota del Pedido (opcional)")
    pedido_total = models.FloatField(verbose_name="Total del Pedido")
    impuesto = models.FloatField(verbose_name="Impuesto")
    status = models.CharField(max_length=50, choices=STATUS, default='New', verbose_name="Estado")
    ip = models.CharField(blank=True, max_length=20, verbose_name="Dirección IP")
    is_ordered = models.BooleanField(default=False, verbose_name="¿Pedido realizado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")


    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'
    nombre_completo.short_description = "Nombre Completo"

    def direccion_completa(self):
        return f'{self.direccion_1} {self.direccion_2}'
    direccion_completa.short_description = "Dirección Completa"

    def __str__(self):
        return self.nombre

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='productos', verbose_name="Pedido")
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Pago")
    user = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name="Usuario")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    producto_precio = models.FloatField(verbose_name="Precio del Producto")
    ordered = models.BooleanField(default=False, verbose_name="¿Pedido Confirmado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    def __str__(self):
        return self.producto.producto_nombre
