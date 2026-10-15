from django.shortcuts import render, get_object_or_404
from .models import InventarioStock, Transferencia

# Create your views here.
def movimientos_stock(request):
    movimientos_stock = InventarioStock.objects.all().order_by('id')
    context = {'movimientos_stock': movimientos_stock}

    if request.htmx:
        return render(request, 'movimientos/partials/lista_movimientos.html', context)

    return render(request, 'movimientos/movimientos_stock.html', context)

def detalle_movimiento(request, pk):
    movimiento = get_object_or_404(InventarioStock, pk=pk)
    context = {'movimiento': movimiento}

    if request.htmx:
            return render(request, 'movimientos/partials/detalle_movimiento.html', context)
    
    return render(request, 'movimientos/detalle_movimientos.html', context )