"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    # 1. Catálogo de Productos
    # path('productos/', include(('apps.productos.urls', 'productos'), namespace='productos')),
    # # 2. Categorías y Marcas
    # path('categorias/', include(('apps.categorias.urls', 'categorias'), namespace='categorias')),
    # # 3. Proveedores
    # path('proveedores/', include(('apps.proveedores.urls', 'proveedores'), namespace='proveedores')),
    # # 4. Clientes
    # path('clientes/', include(('apps.clientes.urls', 'clientes'), namespace='clientes')),
    # # 5. Almacenes / Bodegas
    # path('almacenes/', include(('apps.almacenes.urls', 'almacenes'), namespace='almacenes')),
    # # 6. Compras y Entradas
    # path('compras/', include(('apps.compras.urls', 'compras'), namespace='compras')),
    # # 7. Ventas y Salidas
    # path('ventas/', include(('apps.ventas.urls', 'ventas'), namespace='ventas')),
    # # 8. Movimientos y Stock
    # path('movimientos/', include(('apps.movimientos.urls', 'movimientos'), namespace='movimientos')),
    # # 9. Reportes y Métricas
    # path('reportes/', include(('apps.reportes.urls', 'reportes'), namespace='reportes')),
]
