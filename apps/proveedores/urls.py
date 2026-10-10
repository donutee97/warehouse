from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:pk>/', views.detalle, name='detalle'),
    path('crear/', views.crear , name='crear'),
    path('actualizar/<int:pk>/', views.actualizar, name='actualizar'),
    path('eliminar/<int:pk>', views.eliminar, name='eliminar'),
]
