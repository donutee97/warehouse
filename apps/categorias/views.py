from django.shortcuts import get_object_or_404, render, redirect
from .models import Categorias

def lista_categorias(request):
    categoria = Categorias.objects.order_by('nombre')
    return render(request, 'categorias/lista_categorias.html', {'categorias': categoria})

def detalle(request, pk):
    categoria = get_object_or_404(Categorias, pk=pk)
    return render(request, 'categorias/detalle.html', {'categoria': categoria})


def crear(request):
    if request.method == 'POST':
        Categorias.objects.create(
            nombre= request.POST.get('nombre'),
            descripcion= request.POST.get('descripcion'),
        )
        return redirect('categorias:lista_categorias')
    return render(request, 'categorias/crear.html')