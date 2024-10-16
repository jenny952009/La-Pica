from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MiCuentaManager(BaseUserManager):
    def create_user(self, nombre, apellido, username, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email.')

        if not username:
            raise ValueError('El usuario debe tener un username.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            nombre=nombre,
            apellido=apellido,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, apellido, email, username, password):
        user = self.create_user(
            nombre=nombre,
            apellido=apellido,
            email=email,
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Cuenta(AbstractBaseUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=55)
    username = models.CharField(max_length=50, unique=True)  # Asegúrate de que sea 'username'
    email = models.EmailField(max_length=50, unique=True)
    telefono = models.CharField(max_length=50)

    # Campos atributos
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido']

    objects = MiCuentaManager()

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UsuarioPerfil(models.Model):
    user = models.OneToOneField(Cuenta, on_delete=models.CASCADE)  # Se elimina el perfil al eliminar el usuario
    direccion_1 = models.CharField(blank=True, max_length=100)
    direccion_2 = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    ciudad = models.CharField(blank=True, max_length=20)
    region = models.CharField(blank=True, max_length=20)
    pais = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.nombre

    def direccion_completa(self):
        return f'{self.direccion_1} {self.direccion_2}'
