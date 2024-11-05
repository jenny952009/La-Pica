from django.shortcuts import render, redirect, get_object_or_404
from .forms import SuscripcionForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Suscripcion  # Asegúrate de importar el modelo
from django.http import HttpResponse

def suscribir(request):
    if request.method == 'POST':
        form = SuscripcionForm(request.POST)
        
        if form.is_valid():
            # Guardar la suscripción en la base de datos
            suscripcion = form.save()

            # Enviar el correo de confirmación
            email_cliente = form.cleaned_data['email']
            send_mail(
                'Confirmación de Suscripción',
                f'Hola, \n\nGracias por suscribirte a las exquisitas ofertas de "La Pica de la Chabelita".\n'
                f'Tenemos ofertas semanales para ti. Haz clic en el siguiente enlace para visitarnos: '
                f'http://127.0.0.1:8000/\n\n'
                f'Si ya no deseas recibir nuestros correos, haz clic aquí para desuscribirte: '
                f'http://127.0.0.1:8000/suscripcion/desuscribir/{suscripcion.email}/\n\n'
                f'¡Esperamos verte pronto!',
                settings.DEFAULT_FROM_EMAIL,  # Este debe estar configurado en settings.py
                [email_cliente],  # Enviar al email proporcionado en el formulario
                fail_silently=False,
            )

            # Redirigir a una página de éxito
            return redirect('exito')  # Asegúrate de que la URL 'exito' esté configurada en urls.py
    else:
        form = SuscripcionForm()
    
    # Renderizar el formulario en la página de suscripción
    return render(request, 'suscripcion/suscribir.html', {'form': form})

def exito(request):
    # Renderiza la plantilla de éxito con el mensaje adecuado
    return render(request, 'suscripcion/exito.html')




def desuscribir(request, email):
    try:
        # Intenta encontrar la suscripción con el email proporcionado
        suscripcion = Suscripcion.objects.get(email=email)
        suscripcion.delete()  # Eliminar la suscripción
        # Renderizar la plantilla de desuscripción exitosa
        return render(request, 'suscripcion/desuscrito.html')
    except Suscripcion.DoesNotExist:
        # Si no se encuentra la suscripción, devolver un mensaje
        return HttpResponse("No se encontró la suscripción para este correo.")