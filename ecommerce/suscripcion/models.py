from django.db import models

# Create your models here.
# suscripcion/models.py

class Suscripcion(models.Model):
    email = models.EmailField(unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)  # Campo para activar/desactivar la suscripción

    def __str__(self):
        return self.email
