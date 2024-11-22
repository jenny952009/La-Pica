from django.db.models import Sum, Count
from django.shortcuts import render
from .models import Venta
from django.utils import timezone

def ventas_por_estado():
    return Venta.objects.values('estado_pedido').annotate(total=Sum('total_venta')).order_by('-total')

def ventas_por_region():
    return Venta.objects.values('region').annotate(total=Sum('total_venta')).order_by('-total')

def ventas_por_pais():
    return Venta.objects.values('pais').annotate(total=Sum('total_venta')).order_by('-total')

def cupones_usados():
    return Venta.objects.values('cupon__codigo').annotate(total_ventas=Count('id'), total_descuentos=Sum('cupon__descuento')).order_by('-total_ventas')


# Vista para mostrar las ventas diarias
# Vista para mostrar las ventas diarias
def ventas_diarias(request):
    # Obtener la fecha de hoy
    today = timezone.now().date()
    
    # Filtrar las ventas del día actual
    ventas_data = Venta.objects.filter(fecha__date=today).aggregate(total_ventas=Sum('total_venta'))
     # Sumar el total de ventas del día
    total_ventas = ventas_data.aggregate(total=Sum('total_venta'))['total']

    # Si no hay ventas, asignamos un valor predeterminado (0)
    if total_ventas is None:
        total_ventas = 0
        
    return render(request, 'ventas/ventas_diarias.html', {'ventas': ventas_data, 'total_ventas': total_ventas})
