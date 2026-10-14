from django.urls import path
from . import views

app_name = 'movimientos'

urlpatterns = [
    path('', views.movimientos_stock, name='movimientos_stock'),
    path('<int:pk>/', views.detalle_movimiento, name="detalle")
]
