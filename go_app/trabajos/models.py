from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TrabPresupuesto(models.Model):
    TERMINACION_CHOICES = [
        ('nada', 'Nada'),
        ('troquel', 'Troquel'),
        ('laminado', 'Laminado'),
        ('corte', 'Corte'),
    ]

    empresa = models.CharField(max_length=255)
    nombre_trabajo = models.CharField(max_length=255)
    detalle = models.TextField(blank=True, null=True)
    original_presupuesto = models.ForeignKey('cotizacion.presupuesto', on_delete=models.SET_NULL, null=True)
    fecha_emision = models.DateField()
    fecha_ok = models.DateField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='presupuestos_trabajos')

    class Meta:
        db_table = 'trabajo_presupuesto'
        managed = False  # Evita que Django intente gestionar esta tabla


class TrabProducto(models.Model):
    presupuesto = models.ForeignKey(TrabPresupuesto, related_name='productos_trabajo', on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    cantidad_pliego = models.PositiveIntegerField()
    medida_ancho = models.FloatField()
    medida_alto = models.FloatField()
    papel = models.CharField(max_length=255)
    terminacion = models.CharField(max_length=50, choices=TrabPresupuesto.TERMINACION_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    detalle_producto = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'trabajo_producto'
        managed = False  # Evita que Django intente gestionar esta tabla