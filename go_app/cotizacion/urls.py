from rest_framework import routers
from .api import CotizacionPresupuestoViewSet, CotizacionProductoViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/cotizacion', CotizacionProductoViewSet)
router.register('api/cotizacion', CotizacionPresupuestoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
#aa