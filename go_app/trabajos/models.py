from django.db import models
from cotizacion.models import Presupuesto


class OrdenTrabajo(models.Model):
    Orden_trabajo =  models.ForeignKey(Presupuesto, related_name='productos', on_delete=models.CASCADE)
    


"""class TrabajoPresupuesto(models.Model):
    nombre = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    original_presupuesto = models.ForeignKey(Presupuesto, on_delete=models.SET_NULL, null=True)

class TrabajoProducto(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    trabajo_presupuesto = models.ForeignKey(TrabajoPresupuesto, related_name='trabajo_productos', on_delete=models.CASCADE)"""