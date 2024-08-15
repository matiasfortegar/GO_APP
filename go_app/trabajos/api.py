from rest_framework import viewsets
from .models import OrdenTrabajo
from .serializers import OrdenTrabajoSerial
#from .models import TrabajoPresupuesto, TrabajoProducto
from cotizacion.models import Presupuesto


class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerial




"""def duplicar_presupuesto_a_trabajos(presupuesto_id):
    presupuesto = Presupuesto.objects.get(id=presupuesto_id)
    
    if not presupuesto.aprobado:
        return "El presupuesto no está aprobado."

    trabajo_presupuesto = TrabajoPresupuesto.objects.create(
        nombre=presupuesto.nombre_trabajo,
        empresa=presupuesto.empresa,
        original_presupuesto=presupuesto
    )

    for producto in presupuesto.producto_set.all():
        TrabajoProducto.objects.create(
            nombre=producto.nombre_producto,
            cantidad=producto.cantidad,
            m_alto=producto.medida_alto,
            m_ancho=producto.medida_ancho,
            papel=producto.papel
            trabajo_presupuesto=trabajo_presupuesto
        )

    return trabajo_presupuesto """