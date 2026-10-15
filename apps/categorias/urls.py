from django.urls import path
from . import views

app_name= 'categorias'

urlpatterns = [
    path('', views.lista_categorias, name='lista_categorias'),
    path('<int:pk>', views.detalle, name='detalle'),
    path('crear/', views.crear, name='crear'),
]
