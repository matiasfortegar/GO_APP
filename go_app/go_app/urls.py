"""go_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app_back_end import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('trabajos/', views.trabajos, name='trabajos'),
    path('presupuestos/', views.presupuestos, name='presupuestos'),
    path('presupuestos/<int:presupuesto_id>/agregar_productos/', views.agregar_productos, name='agregar_productos'),
    path('presupuestos/<int:presupuesto_id>/', views.presupuestos_detalle, name='presupuestos_detalle'),
    path('trabajos/<int:presupuesto_id>/duplicar/', views.duplicar_presupuesto, name='duplicar_presupuesto'),
    path('crear_presupuestos/', views.crear_presupuestos, name='crear_presupuestos'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('login/', views.iniciar_sesion, name='login'),
    #path('', include('cotizacion.urls')),
    #path('trabajos/', include('trabajos.urls')),    


]
