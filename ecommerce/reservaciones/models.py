from django.db import models

# Create your models here.

""""
CODIGO ENRIQUE
class Reserva(models.Model):
    #codigo_reserva = models.CharField(max_length=100)
    codigo_reserva = models.CharField(max_length=100, default='DEFAULT_CODE')  # Cambia 'DEFAULT_CODE' por un valor que prefieras
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    numero_mesa = models.IntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    hora_comienzo = models.TimeField()
    personas = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Mesa {self.numero_mesa}"
        
        """

from django.db import models
from django.utils import timezone
import uuid

class Reserva(models.Model):
    # Genera un código único para la reserva
    codigo_reserva = models.CharField(max_length=100, default=uuid.uuid4, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    numero_mesa = models.IntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)  # Se establece al crear el objeto
    hora_comienzo = models.TimeField()
    personas = models.IntegerField()
    dia_reserva = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Mesa {self.numero_mesa}"
