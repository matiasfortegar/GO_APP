"""from rest_framework import viewsets, permissions
from .models import Presupuesto, Producto
from .serializers import CotizacionPresupuesto, CotizacionProducto

class CotizacionPresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CotizacionPresupuesto

class CotizacionProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CotizacionProducto
"""
