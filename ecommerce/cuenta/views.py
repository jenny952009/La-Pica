from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrarForm, UsuarioPerfilForm, UsuarioForm
from .models import Cuenta, UsuarioPerfil
from pedido.models import Pedido
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from carrito.views import _carrito_id
from carrito.models import Carrito, CarritoItem
from datetime import datetime, timedelta
import requests
import re


# Esta función maneja el registro de nuevos usuarios y envía un email de verificación.
def registrar(request):
    form = RegistrarForm()
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            # Validación del número de teléfono
            telefono = form.cleaned_data['telefono']
            if not re.match(r'^\d{9}$', telefono):  # Solo acepta 9 dígitos
                messages.error(request, 'El número de teléfono debe tener exactamente 9 dígitos.')
                return render(request, 'cuenta/registrar.html', {'form': form})

            # Creación de la cuenta de usuario y perfil
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Cuenta.objects.create_user(
                nombre=nombre, apellido=apellido, email=email, username=username, password=password
            )
            user.telefono = telefono
            user.save()

            profile = UsuarioPerfil()
            profile.user_id = user.id
            profile.profile_picture = 'default/default-user.png'
            profile.save()

            # Envío de correo de verificación
            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta en La Pica de la Chabelita para continuar'
            body = render_to_string('cuenta/cuenta_verificacion_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_email = EmailMessage(mail_subject, body, to=[email])
            send_email.send()

            return redirect('/cuenta/login/?command=verification&email=' + email)

    context = {
        'form': form
    }
    return render(request, 'cuenta/registrar.html', context)

# Diccionario para llevar el seguimiento de intentos fallidos y bloqueo temporal
intentos_fallidos = {}

def login(request):
    global intentos_fallidos
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Verificar si el usuario está temporalmente bloqueado
        if email in intentos_fallidos:
            bloqueo = intentos_fallidos[email].get('bloqueo')
            if bloqueo and bloqueo > datetime.now():
                tiempo_restante = (bloqueo - datetime.now()).seconds  # Segundos restantes del bloqueo
                messages.error(request, f'¡Demasiados intentos! Tu cuenta está bloqueada temporalmente por {tiempo_restante} segundos.')
                return redirect('login')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            # Restablecer los intentos fallidos si el inicio de sesión es exitoso
            if email in intentos_fallidos:
                del intentos_fallidos[email]

            try:  # Comprobación y actualización del carrito en caso de items previos.
                carro = Carrito.objects.get(carrito_id=_carrito_id(request))
                is_carrito_item_exist = CarritoItem.objects.filter(carro=carro).exists()

                if is_carrito_item_exist:
                    carrito_item = CarritoItem.objects.filter(carro=carro)

                    producto_variacion = []

                    for item in carrito_item:
                        variacion = item.variacion.all()
                        producto_variacion.append(list(variacion))

                    carrito_item = CarritoItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []

                    for item in carrito_item:
                        existing_variation = item.variacion.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)

                    for pr in producto_variacion:
                        if pr in ex_var_list:
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CarritoItem.objects.get(id=item_id)
                            item.cantidad += 1
                            item.user = user
                            item.save()
                        else:
                            carrito_item = CarritoItem.objects.filter(carro=carro)
                            for item in carrito_item:
                                item.user = user
                                item.save()

            except:
                pass

            auth.login(request, user)
            messages.success(request, 'Has iniciado sesión exitosamente')

            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')

        else:
            # Registrar intentos fallidos
            if email not in intentos_fallidos:
                intentos_fallidos[email] = {'intentos': 1, 'bloqueo': None}
            else:
                intentos_fallidos[email]['intentos'] += 1

            # Bloquear la cuenta después de 5 intentos fallidos
            if intentos_fallidos[email]['intentos'] >= 5:
                intentos_fallidos[email]['bloqueo'] = datetime.now() + timedelta(seconds=30)
                messages.error(request, '¡Demasiados intentos! Tu cuenta está bloqueada temporalmente por 30 segundos.')
            else:
                messages.error(request, 'Los datos son incorrectos')

            return redirect('login')

    return render(request, 'cuenta/login.html')

                
# Esta función permite cerrar sesión en el sistema y redirige al login.
               
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Has salido de sesión')
    return redirect('login')

# Función para activar la cuenta del usuario mediante un enlace de verificación en el correo.
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Cuenta._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Cuenta.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Felicidades, tu cuenta está activa!')
        return redirect('login')
    else:
        messages.error(request, 'No se pudo completar la activación de la cuenta')
        return redirect('registrar')
    
# Muestra un panel de usuario con sus pedidos y detalles de perfil.
@login_required(login_url='login')
def dashboard(request):
        
    pedidos = Pedido.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    pedido_count = pedidos.count()
    
    userprofile = UsuarioPerfil.objects.get(user_id=request.user.id)

    context = {
        'pedido_count': pedido_count,
        'userprofile': userprofile,
    }

    return render(request, 'cuenta/dashboard.html', context)

# Esta función gestiona el proceso de recuperación de contraseña a través de email.
def olvidarPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Cuenta.objects.filter(email=email).exists():
            user = Cuenta.objects.get(email__exact=email)

            current_site = get_current_site(request)
            mail_subject = 'Recupera tu Contraseña'
            body = render_to_string('cuenta/borrar_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()

            messages.success(request, 'Un email fue enviado a tu bandeja de entrada para recuperar tu contraseña')
            return redirect('login')
        else:
            messages.error(request, 'La cuenta de usuario no existe o surgió un problema')
            return redirect('olvidarPassword')

    return render(request, 'cuenta/olvidarPassword.html')

# Esta función valida el enlace de recuperación de contraseña y permite reestablecerla.
def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Cuenta._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Cuenta.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Por favor escribe tu nueva contraseña')
        return redirect('borrarPassword')
    else:
        messages.error(request, 'El link ha caducado')
        return redirect('login')

# Permite al usuario reestablecer su contraseña si el token es válido.
def borrarPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirmar_password = request.POST['confirmar_password']

        if password == confirmar_password:
            uid = request.session.get('uid')
            user = Cuenta.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'La contraseña se actualizó correctamente')
            return redirect('login')
        else:
            messages.error(request, 'La contraseña de confirmación no es igual')
            return redirect('borrarPassword')
    else:    
        
         return render(request, 'cuenta/borrarPassword.html')

# Muestra una lista de pedidos realizados por el usuario.
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'pedidos': pedidos,
    }

    return render(request, 'cuenta/mis_pedidos.html', context)

# Permite al usuario editar su perfil y guardar los cambios.
@login_required(login_url='login')
def editar_perfil(request):
    userprofile = get_object_or_404(UsuarioPerfil, user=request.user)
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST, instance=request.user)
        profile_form = UsuarioPerfilForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Su información fue guardada con éxito')
            return redirect('editar_perfil')
    else:
        user_form = UsuarioForm(instance=request.user)
        profile_form = UsuarioPerfilForm(instance=userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }

    return render(request, 'cuenta/editar_perfil.html', context)

@login_required(login_url='login')# Esta función permite al usuario cambiar su contraseña tras verificar la actual.
def cambio_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirmar_password = request.POST['confirmar_password']

        user = Cuenta.objects.get(username__exact=request.user.username)

        if new_password == confirmar_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()

                messages.success(request, 'La contraseña se actualizó correctamente')
                return redirect('cambio_password')
            else:
                messages.error(request, 'Los datos no son válidos, ingresa una contraseña correcta')
                return redirect('cambio_password')
        else:
            messages.error(request, 'La contraseña no coincide con la confirmación')
            return redirect('cambio_password')

    return render(request, 'cuenta/cambio_password.html')
 
            
#-----------------------------ayuda_y_contacto.html-------------------------------------------   

@login_required(login_url='login')
def ayuda_y_contacto(request):
    return render(request, 'cuenta/ayuda_y_contacto.html')    