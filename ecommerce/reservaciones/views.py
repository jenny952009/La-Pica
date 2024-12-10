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

        # Calcular la hora de fin sumando 1 hora a la hora de comienzo
        hora_comienzo_obj = datetime.strptime(hora_comienzo, "%H:%M")
        hora_fin_obj = hora_comienzo_obj + timedelta(hours=1)
        hora_fin = hora_fin_obj.strftime("%H:%M")

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

        # Verificar si la mesa ya está ocupada para el día y hora seleccionados
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

        # Verificar si el correo ya ha realizado una reserva, independientemente de la mesa, hora o día
        correo_existente = Reserva.objects.filter(email=email).exists()

        if correo_existente:
            return JsonResponse({
                'error': 'correo_existente',
                'error_msg': "¡Lo sentimos! El correo electrónico ingresado ya ha realizado una reserva previamente."
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
            hora_fin=hora_fin,  # Guardar la hora de fin en la base de datos
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

        # Buscar la reserva por código
        reserva = Reserva.objects.filter(codigo_reserva=codigo_reserva).first()

        if reserva:
            # Formatear la fecha de reserva
            fecha_reserva_formateada = reserva.fecha_reserva.strftime('%Y-%m-%d')
            
            html = f"""
            <html>
            <div style="text-align: center;">
            <img src="static/images/icons/Icono.jpeg" alt="Logo del restaurante" style="width:150px;height:auto;"> <!-- Agregado: Imagen -->
            </div>
                    </div>
                        <hr />
                    </div>              
                <head>
                    <title>Ticket de reserva</title>
                    <link rel="stylesheet" type="text/css" href="static/css/ticket.css"> <!-- Enlace del archivo CSS a ticket.css-->
                </head>
                <body>
                    <h1>Detalles de la Reserva</h1>
                    <p>Nombre del cliente: {reserva.nombre}</p>
                    <p>Apellido del cliente: {reserva.apellido}</p>
                    <p>Código de la Reservación : {reserva.codigo_reserva}</p>
                    </div>
                        <hr />
                    </div>
                    <p>Email del Cliente: {reserva.email}</p>
                    <p>Teléfono del Cliente: {reserva.telefono}</p>
                    <p>Fecha en la que se hizo la Reservación: {fecha_reserva_formateada}</p>
                    </div>
                        <hr />
                    </div>
                    <p>N. de Mesa Reservada: {reserva.numero_mesa}</p>
                    <p>Hora de Comienzo de la Reservación de la mesa: {reserva.hora_comienzo} HRS.</p>
                    <p>Hora de Término de la Reservación de la mesa: {reserva.hora_fin} HRS.</p>
                    <p>N. de Personas totales de la Reserva: {reserva.personas}</p>
                    <p>Día de la Reservación: {reserva.dia_reserva}</p>
                    </div>
                        <hr />
                    </div> 
                    <p class="text-small"> Estimado cliente, el siguiente ticket es válido hasta la fecha en la que su mesa fue reservada. No nos hacemos responsables de reclamos o devoluciones después de la fecha estimada.¡Gracias por su atención! Para más información, contáctenos a nuestro número +569 1111 1111.</p>
                    </div>
                        <hr />
                    </div>                                          
                </body>
            </html>
            """

            # Generar el archivo PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="ticket_reserva.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)

            if pisa_status.err:
                return HttpResponse('Hubo un error al generar el PDF.')
            return response
        else:
            # Si no se encuentra la reserva, renderizar nuevamente con el error
            return render(request, 'reservaciones/reservacion.html', {
                'error_msg': 'Código de reserva no encontrado. Por favor, intenta nuevamente.'
            })
    return redirect('reservacion')  # Redirigir si no es un método POST
