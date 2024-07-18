from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Presupuesto(models.Model):
    TERMINACION_CHOICES = [
        ('troquel', 'Troquel'),
        ('laminado', 'Laminado'),
        ('corte', 'Corte'),
    ]

    empresa = models.CharField(max_length=255)
    nombre_trabajo = models.CharField(max_length=255)
    detalle = models.TextField(blank=True, null=True)
    aprobado = models.BooleanField(default=False)
    fecha_emision = models.DateField()
    fecha_ok = models.DateField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.aprobado and not self.fecha_ok:
            self.fecha_ok = timezone.now().date()
        elif not self.aprobado:
            self.fecha_ok = None
        super(Presupuesto, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.empresa} - {self.nombre_trabajo}"

class Producto(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, related_name='mas_productos', on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    cantidad_pliego = models.PositiveIntegerField()
    medida_ancho = models.FloatField()
    medida_alto = models.FloatField()
    papel = models.CharField(max_length=255)
    terminacion = models.CharField(max_length=50, choices=Presupuesto.TERMINACION_CHOICES)
    valor = models.PositiveIntegerField()
    detalle_producto = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_producto} ({self.presupuesto})"