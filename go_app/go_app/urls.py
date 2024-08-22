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
    path('presupuestos/', views.Presupuestos, name='presupuestos'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('login/', views.iniciar_sesion, name='login'),
    path('agregar_presupuesto/', views.agregar_producto, name='agregar_presupuesto'),
    path('crear_presupuesto/', views.crear_presupuesto, name='crear_presupuesto'),
    path('trabajos/', views.crear_trabajo, name='trabajos'),
    path('', include('cotizacion.urls')),
    path('', include('trabajos.urls')),


]
