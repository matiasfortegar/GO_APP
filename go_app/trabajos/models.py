from django.db import models
from cotizacion.models import Presupuesto

class OrdenTrabajo(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
    nombre_trabajo = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    fecha_ok = models.DateField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.empresa} - {self.nombre_trabajo}"

"""
    def save(self, *args, **kwargs):
        # Copiar datos del presupuesto al crear una nueva orden de trabajo
        if not self.id: # type: ignore
            self.nombre_trabajo = self.presupuesto.nombre_trabajo
            self.empresa = self.presupuesto.empresa
            self.fecha_ok = self.presupuesto.fecha_ok
        super(OrdenTrabajo, self).save(*args, **kwargs)

"""

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


"""
    def save(self, *args, **kwargs):
        if not self.id: # type: ignore
            presupuesto_producto = Producto.objects.get(id=self.id) # type: ignore
            self.nombre_producto = presupuesto_producto.nombre_producto
            self.cantidad = presupuesto_producto.cantidad
            self.cantidad_pliego = presupuesto_producto.cantidad_pliego
            self.medida_ancho = presupuesto_producto.medida_ancho
            self.medida_alto = presupuesto_producto.medida_alto
            self.papel = presupuesto_producto.papel
            self.terminacion = presupuesto_producto.terminacion
            self.valor = presupuesto_producto.valor
            self.detalle_producto = presupuesto_producto.detalle_producto
        super(ProductoOrden, self).save(*args, **kwargs)

"""