from rest_framework import routers
from .api import CotizacionPresupuestoViewSet, CotizacionProductoViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/pres_producto', CotizacionProductoViewSet)
router.register('api/presupuesto', CotizacionPresupuestoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
#aa
 