from rest_framework import viewsets, permissions
from .models import OrdenTrabajo
from .serializers import OrdenTrabajoSerial

class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrdenTrabajoSerial