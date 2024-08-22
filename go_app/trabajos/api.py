from rest_framework import viewsets
from .models import TrabPresupuesto, TrabProducto
from .serializers import TrabajopresupuestoSerial, TrabajoproductoSerial
#from .models import Trabajopresupuesto, Trabajoproducto


class TrabajopresupuestoViewSet(viewsets.ModelViewSet):
    queryset = TrabPresupuesto.objects.all()
    serializer_class = TrabajopresupuestoSerial

class TrabajoproductoViewSet(viewsets.ModelViewSet):
    queryset = TrabProducto.objects.all()
    serializer_class = TrabajoproductoSerial