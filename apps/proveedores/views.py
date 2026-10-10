from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor

# Create your views here.
def lista(request):
    proveedores = Proveedor.objects.all().order_by('id')
    return render(request, 'proveedores/lista.html', {'proveedores': proveedores})

def detalle(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedores/detalle.html', {'proveedor': proveedor})

def crear(request):
    if request.method == "POST":
        Proveedor.objects.create(
            razon_social=request.POST.get('razon_social'),
            nit_rut=request.POST.get('nit_rut'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono')
        )
        return redirect('proveedores:lista')
    
    return render(request, 'proveedores/crear.html')

def actualizar(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == "POST":
        proveedor.razon_social = request.POST.get('razon_social')
        proveedor.nit_rut = request.POST.get('nit_rut')
        proveedor.email = request.POST.get('email')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.save()
        
        return redirect('proveedores:lista')
    
    return render(request, 'proveedores/actualizar.html', {'proveedor': proveedor})

def eliminar(request, pk):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, pk=pk)
        proveedor.delete()
    return redirect('proveedores:lista')