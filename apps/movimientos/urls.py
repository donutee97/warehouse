from django.urls import path
from . import views

app_name = 'movimientos'

urlpatterns = [
    path('', views.listar, name='listar'),
    path('<int:pk>/', views.detalle, name="detalle"),
    path('crear', views.crear, name="crear")
]
