from django.db import models
from cuenta.models import Cuenta
from tienda.models import Producto
from pedido.models import Pedido, Pago
from django.utils import timezone  # Añadir esta importación al principio del archivo

class EstadoPedido(models.TextChoices):
    NUEVO = 'New', 'Nuevo'
    EN_PROCESO = 'In Progress', 'En proceso'
    ENVIADO = 'Shipped', 'Enviado'
    ENTREGADO = 'Delivered', 'Entregado'


class Cupon(models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código del cupón")
    descuento = models.FloatField(verbose_name="Porcentaje de descuento")
    activo = models.BooleanField(default=True, verbose_name="¿Está activo?")
    fecha_expiracion = models.DateTimeField(verbose_name="Fecha de expiración")

    def __str__(self):
        return self.codigo
    def es_valido(self):
        return self.activo and self.fecha_expiracion > timezone.now()


class Venta(models.Model):
    user = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name="Usuario")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name="Pedido relacionado")
    pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, null=True, verbose_name="Método de pago")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    total_venta = models.FloatField(verbose_name="Total de la venta")
    cupon = models.ForeignKey(Cupon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cupón aplicado")
    estado_pedido = models.CharField(max_length=50, choices=EstadoPedido.choices, default=EstadoPedido.NUEVO)
    region = models.CharField(max_length=50, verbose_name="Región")
    pais = models.CharField(max_length=50, verbose_name="País")
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la venta")

    def __str__(self):
        return f"{self.producto} - {self.user.email}"

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

