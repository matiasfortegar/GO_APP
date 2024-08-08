from rest_framework import viewsets
from .models import OrdenTrabajo
from .serializers import OrdenTrabajoSerial

class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerial