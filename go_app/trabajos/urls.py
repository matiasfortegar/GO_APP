from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import OrdenTrabajoViewSet

router = DefaultRouter()
router.register(r'ordenes', OrdenTrabajoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]