from rest_framework import routers
from .api import OrdenTrabajoViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/OrdenTrabajo', OrdenTrabajoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
#aa