from django.shortcuts import render, get_object_or_404
from .models import Proveedor

# Create your views here.
def lista(request):

    proveedores = Proveedor.objects.all().order_by('id')

    return render(request, 'proveedores/lista.html', {'proveedores': proveedores})

def detalle(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedores/detalle.html', {'proveedor': proveedor})