from django.db import models
from django.utils import timezone
import uuid

class Reserva(models.Model):
    # Genera un código único para la reserva
    codigo_reserva = models.CharField(max_length=100, default=uuid.uuid4, unique=True, verbose_name="Código de Reserva")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    numero_mesa = models.IntegerField(verbose_name="Número de Mesa")
    fecha_reserva = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Reserva")
    hora_comienzo = models.CharField(max_length=100, verbose_name="Hora de Comienzo")
    hora_fin = models.CharField(max_length=100, verbose_name="Hora de Fin")
    personas = models.IntegerField(verbose_name="Número de Personas")
    dia_reserva = models.DateField(default=timezone.now, verbose_name="Día de Reserva")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Mesa {self.numero_mesa}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
