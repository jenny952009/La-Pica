from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from xhtml2pdf import pisa
import random
import string

# Función para generar código de reserva aleatorio
def generar_codigo_reserva():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Vista para manejar la reserva
def reservacion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        numero_mesa = request.POST.get('numero_mesa')
        hora_comienzo = request.POST.get('hora_comienzo')
        personas = request.POST.get('personas')
        
        # Validación para asegurarse de que los campos no estén vacíos
        if not nombre:
            return JsonResponse({'error': 'El nombre no puede estar vacío.'}, status=400)
        if not apellido:
            return JsonResponse({'error': 'El apellido no puede estar vacío.'}, status=400)
        if not email:
            return JsonResponse({'error': 'El correo electrónico no puede estar vacío.'}, status=400)

        # Generar un código de reserva
        codigo_reserva = generar_codigo_reserva()

        # Guarda la reserva en la base de datos
        Reserva.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            numero_mesa=numero_mesa,
            fecha_reserva=datetime.now(),
            hora_comienzo=hora_comienzo,
            personas=personas,
            codigo_reserva=codigo_reserva
        )

        # Retorna un mensaje de éxito en formato JSON
        return JsonResponse({'success': 'Reserva creada con éxito.', 'codigo_reserva': codigo_reserva})

    return render(request, 'reservaciones/reservacion.html')


# Vista para descargar la boleta en PDF
@csrf_exempt
def descargar_boleta(request):
    if request.method == 'POST':
        codigo_reserva = request.POST.get('codigo_reserva')
        
        # Buscar la reserva por el código de reserva
        reserva = Reserva.objects.filter(codigo_reserva=codigo_reserva).first()
        
        if reserva:
            # Generar el contenido del PDF
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
                </body>
            </html>
            """
            
            # Crea el PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="boleta_{codigo_reserva}.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            
            if pisa_status.err:
                return JsonResponse({'error': 'Error al generar el PDF'}, status=500)
                
            return response
        else:
            return JsonResponse({'error': 'Código de reserva no encontrado.'}, status=404)

    return JsonResponse({'error': 'Método no permitido.'}, status=405)
