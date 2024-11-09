from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from xhtml2pdf import pisa
from django.utils import timezone
from django.core.validators import validate_email
from django.utils.dateparse import parse_datetime
from django.core.exceptions import ValidationError
import random
import string


# Función para generar código de reserva aleatorio
def generar_codigo_reserva():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


def reservacion(request):
    # Generar los próximos cinco días para el selector de días
    days = [(timezone.now() + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, 6)]
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        numero_mesa = request.POST.get('numero_mesa')
        hora_comienzo = request.POST.get('hora_comienzo')
        personas = request.POST.get('personas')
        dia_reserva = request.POST.get('dia_reserva')

        # Validación de campos vacíos
        if not nombre:
            return JsonResponse({'error': 'El nombre no puede estar vacío.'}, status=400)
        if not apellido:
            return JsonResponse({'error': 'El apellido no puede estar vacío.'}, status=400)
        if not email:
            return JsonResponse({'error': 'El correo electrónico no puede estar vacío.'}, status=400)

        # Validación del correo electrónico
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'error': 'Correo electrónico no es válido.'}, status=400)

        # Verificar si la mesa está ocupada para el día y hora seleccionados
        reserva_existente = Reserva.objects.filter(
            numero_mesa=numero_mesa,
            dia_reserva=dia_reserva,
            hora_comienzo=hora_comienzo
        ).exists()

        if reserva_existente:
            return JsonResponse({
                'error': 'mesa_ocupada',
                'error_msg': "¡Lo sentimos! pero la mesa que intentas reservar ya está reservada."
            }, status=400)

        # Generar código de reserva
        codigo_reserva = generar_codigo_reserva()

        # Crear la reserva
        Reserva.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            numero_mesa=numero_mesa,
            fecha_reserva=timezone.now(),
            hora_comienzo=hora_comienzo,
            personas=personas,
            codigo_reserva=codigo_reserva,
            dia_reserva=dia_reserva
        )

        # Enviar correo electrónico de confirmación
        mail_subject = 'Felicidades, Has reservado tu mesa en La Pica de la Chabelita'
        body = f"""
        ¡Felicidades, {nombre} {apellido}!

        Has reservado tu mesa. Aquí tienes tu código de reserva: {codigo_reserva}

        Pasos a seguir para descargar el ticket:

        1. Ve a la página principal de reservaciones y en el apartado "Descargar ticket de reserva", ingresa el código y luego presiona "Sacar ticket".
        
        2. Luego de descargar tu ticket, tienes que mostrar el ticket en el restaurante La Pica de la Chabelita.
        
        3. Cuando muestres tu ticket a la persona encargada, podrás pasar a tu mesa reservada.

        ¡Gracias por elegirnos!
        """
        send_email = EmailMessage(mail_subject, body, to=[email])
        send_email.send()

        # Redirigir en caso de éxito con el correo y el código de reserva
        return JsonResponse({'email': email, 'codigo_reserva': codigo_reserva})

    # Renderizar la página de reservaciones
    return render(request, 'reservaciones/reservacion.html', {'days': days})


@csrf_exempt
def Descargar_Ticket(request):
    if request.method == 'POST':
        codigo_reserva = request.POST.get('codigo_reserva')

        reserva = Reserva.objects.filter(codigo_reserva=codigo_reserva).first()

        if reserva:
            html = f"""
            <html>
                <head>
                    <title>Boleta de Reserva</title>
                </head>
                <body>
                    <h1>Detalles de la Reserva</h1>
                    <p>Código de Reserva: {reserva.codigo_reserva}</p>
                    <p>Nombre: {reserva.nombre}</p>
                    <p>Apellido: {reserva.apellido}</p>
                    <p>Email: {reserva.email}</p>
                    <p>Teléfono: {reserva.telefono}</p>
                    <p>Número de Mesa: {reserva.numero_mesa}</p>
                    <p>Fecha de Reserva: {reserva.fecha_reserva}</p>
                    <p>Hora de Comienzo: {reserva.hora_comienzo}</p>
                    <p>Personas: {reserva.personas}</p>
                    <p>Día de Reserva: {reserva.dia_reserva}</p>
                </body>
            </html>
            """
            
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="boleta_{codigo_reserva}.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            
            if pisa_status.err:
                return JsonResponse({'error': 'Error al generar el PDF'}, status=500)
                
            return response
        else:
            return JsonResponse({'error': 'Código de reserva no encontrado.'}, status=404)

    return JsonResponse({'error': 'Método no permitido.'}, status=405)