from django.shortcuts import render, get_object_or_404
from .models import InventarioStock, Transferencia
from apps.productos.models import Productos
from apps.almacenes.models import Almacen

# Create your views here.
def listar(request):
    movimientos_stock = InventarioStock.objects.all().order_by('id')
    context = {'movimientos_stock': movimientos_stock}

    if request.htmx:
        return render(request, 'movimientos/partials/listado.html', context)

    return render(request, 'movimientos/listar.html', context)

def detalle(request, pk):
    movimiento = get_object_or_404(InventarioStock, pk=pk)
    context = {'movimiento': movimiento}

    if request.htmx:
            return render(request, 'movimientos/partials/detalle.html', context)
    
    return render(request, 'movimientos/detallar.html', context )

def crear(request):
    movimientos = InventarioStock.objects.all()
    productos = Productos.objects.all()
    almacenes = Almacen.objects.all()
    context = {'movimientos': movimientos, 'productos': productos, 'almacenes': almacenes}

    return render(request, 'movimientos/crear.html', context)