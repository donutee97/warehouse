from django.shortcuts import render, get_object_or_404
from .models import Proveedor

# Create your views here.
def lista_proveedores(request):

    proveedores = Proveedor.objects.all().order_by('id')

    return render(request, 'proveedores/lista_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedores/detalle_proveedor.html', {'proveedor': proveedor})