import matplotlib.pyplot as plt # type: ignore
from django.http import HttpResponse
from pedido.models import Pedido  # Importamos el modelo Pedido
from django.db import models

def ventas_por_fecha(request):
    # Obtiene el total de ventas por fecha
    ventas = Pedido.objects.filter(status='Completed').values('created_at').annotate(total=models.Sum('pedido_total'))
    
    # Preparando los datos
    fechas = [venta['created_at'] for venta in ventas]
    totales = [venta['total'] for venta in ventas]

    # Crear el gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(fechas, totales, marker='o', linestyle='-', color='b')
    plt.xlabel('Fecha')
    plt.ylabel('Ventas Totales')
    plt.title('Ventas por Fecha')

    # Convertir el gráfico a imagen y devolverlo como respuesta
    response = HttpResponse(content_type='image/png')
    plt.savefig(response, format="png")
    return response
