from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

#Gestionar cómo se crean tanto usuarios regulares como superusuario
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

#Se definen los campos básicos para la cuenta
class Cuenta(AbstractBaseUser, PermissionsMixin):
    # Campos de la cuenta 
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=55, verbose_name="Apellido")
    username = models.CharField(max_length=50, unique=True, verbose_name="Nombre de usuario")
    email = models.EmailField(max_length=50, unique=True, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=50, verbose_name="Teléfono")

    # Campos atributos
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    last_login = models.DateTimeField(auto_now=True, verbose_name="Último inicio de sesión")
    is_admin = models.BooleanField(default=False, verbose_name="¿Es administrador?")
    is_staff = models.BooleanField(default=False, verbose_name="¿Es staff?")
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")
    is_superadmin = models.BooleanField(default=False, verbose_name="¿Es superadministrador?")

    # Campos adicionales para permisos y grupos
    groups = models.ManyToManyField(
        Group,
        related_name="user_set",
        blank=True,
        help_text="Los grupos a los que pertenece este usuario.",
        verbose_name="grupos",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="user_set",
        blank=True,
        help_text="Permisos específicos para este usuario.",
        verbose_name="permisos de usuario",
    )

    USERNAME_FIELD = 'email' #usuarios inician sesión usando su correo electrónico
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

    class Meta:
        verbose_name = "Cuenta de usuario"
        verbose_name_plural = "Cuentas de usuarios"
        
    #Información de la Cuenta y permite agregar datos de perfil adicionales
class UsuarioPerfil(models.Model):
    user = models.OneToOneField(
        Cuenta, 
        on_delete=models.CASCADE, 
        verbose_name="Usuario"
    )
    direccion_1 = models.CharField(blank=True, max_length=100, verbose_name="Dirección principal")
    direccion_2 = models.CharField(blank=True, max_length=100, verbose_name="Detalle Dirección")
    profile_picture = models.ImageField(
        upload_to='userprofile/', 
        blank=True, 
        default='default_profile.jpg', 
        verbose_name="Foto de Perfil"
    )
    ciudad = models.CharField(blank=True, max_length=20, verbose_name="Ciudad")
    region = models.CharField(blank=True, max_length=20, verbose_name="Región")
    pais = models.CharField(blank=True, max_length=20, verbose_name="País")
    def __str__(self):
        return self.user.nombre

    def direccion_completa(self):
        return f'{self.direccion_1} {self.direccion_2}'.strip()

    class Meta:
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuarios"
