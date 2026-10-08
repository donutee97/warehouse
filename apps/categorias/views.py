from django.shortcuts import render
from .models import Categorias

def lista_categorias(request):
    categoria = Categorias.objects.order_by('nombre')

    return render(request, 'categorias/lista_categorias.html', {'categorias': categoria})