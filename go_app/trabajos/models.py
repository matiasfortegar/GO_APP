from django.db import models
from cotizacion.models import Presupuesto


class OrdenTrabajo(models.Model):
    Orden_trabajo =  models.ForeignKey(Presupuesto, related_name='productos', on_delete=models.CASCADE)
    