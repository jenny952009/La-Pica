from django.db import models
from cuenta.models import Cuenta  # Si AUTH_USER_MODEL apunta a Cuenta

class Empleado(models.Model):
    usuario = models.OneToOneField(Cuenta, on_delete=models.CASCADE, related_name="empleado")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sueldo")
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT del empleado")
    fecha_contrato = models.DateField(verbose_name="Fecha de Contrato")
    activo = models.BooleanField(default=True, verbose_name="Empleado Activo")

     # Horarios
    entrada = models.TimeField(null=True, blank=True, default="00:00",verbose_name="Hora de entrada")
    salida = models.TimeField(null=True, blank=True, default="00:00",verbose_name="Hora de salida")
    entrada_almuerzo = models.TimeField(null=True, blank=True, default="00:00",verbose_name="Entrada de almuerzo")
    salida_almuerzo = models.TimeField(null=True, blank=True, default="00:00",verbose_name="Salida de almuerzo")
    
    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido} - {self.cargo}"
    

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["-fecha_contrato"]
