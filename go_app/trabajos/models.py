from django.db import models
from cotizacion.models import Presupuesto
from django.contrib.auth.models import User

class OrdenTrabajo(models.Model):
    empresa = models.CharField(max_length=255)
    nombre_trabajo = models.CharField(max_length=255)
    detalle = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    presupuesto_original = models.ForeignKey(Presupuesto, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Orden de Trabajo: {self.nombre_trabajo} - {self.empresa}"

class ProductoOrden(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, related_name='productos', on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    cantidad_pliego = models.PositiveIntegerField()
    medida_ancho = models.FloatField()
    medida_alto = models.FloatField()
    papel = models.CharField(max_length=255)
    terminacion = models.CharField(max_length=50, choices=Presupuesto.TERMINACION_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    detalle_producto = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_producto} ({self.orden_trabajo})"

