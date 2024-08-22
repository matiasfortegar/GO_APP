from rest_framework import routers
from .api import TrabajopresupuestoViewSet, TrabajoproductoViewSet
from django.urls import path, include
from .views import duplicar_presupuesto_formulario, ver_presupuesto

router = routers.DefaultRouter()

router.register('api/trabajo_presupusto', TrabajopresupuestoViewSet)
router.register('api/trabajo_producto', TrabajoproductoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('presupuesto/<int:presupuesto_id>/', ver_presupuesto, name='ver_presupuesto'),
    path('presupuesto/<int:presupuesto_id>/', duplicar_presupuesto_formulario, name='duplicar_presupuesto_formulario'),
]
#aa