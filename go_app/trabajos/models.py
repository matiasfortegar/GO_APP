from django.db import models
from cotizacion.models import Presupuesto

# Create your models here.

class OrdenTrabajo(models.Model):
 OT = models.ForeignKey(Presupuesto, related_name='productos', on_delete=models.CASCADE)