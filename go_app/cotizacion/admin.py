from django.contrib import admin
from django.db import transaction, IntegrityError
from .models import Presupuesto, Producto
from trabajos.models import TrabProducto, TrabPresupuesto

# Register your models here.

def duplicar_presupuesto(modeladmin, request, queryset):
    for presupuesto in queryset:
        if presupuesto.aprobado:
            try:
                # Inicia una transacción atómica en la base de datos 'trabajos_db'
                with transaction.atomic(using='trabajos_db'):

            # Crear un nuevo TrabajoPresupuesto en la base de datos 'trabajos_db'
                    nuevo_trabajo_presupuesto = TrabPresupuesto.objects.using('trabajos_db').create(
                        nombre_trabajo=presupuesto.nombre_trabajo,
                        empresa=presupuesto.empresa,
                        detalle=presupuesto.detalle,
                        fecha_ok=presupuesto.fecha_ok,
                        usuario=presupuesto.usuario,

                    )
            
                # Duplicar los productos asociados
                productos = Producto.objects.using('default').filter(presupuesto=presupuesto)
                for producto in productos:
                    TrabProducto.objects.using('trabajos_db').create(
                    presupuesto=nuevo_trabajo_presupuesto,
                    nombre=producto.nombre_producto,
                    cantidad=producto.cantidad,
                    cantidad_pliego=producto.cantidad_pliego,
                    medida_ancho=producto.medida_ancho,
                    medida_alto=producto.medida_alto,
                    papel=producto.papel,
                    terminacion=producto.terminacion,
                    detalle_producto=producto.detalle_producto,
                        
                    )

            except IntegrityError as e:
                modeladmin.message_user(request, f"Error al duplicar: {e}")
                continue

    modeladmin.message_user(request, "Presupuesto(s) duplicado(s) exitosamente en la base de datos de trabajos.")

duplicar_presupuesto.short_description = "Duplicar presupuesto(s) aprobado(s) a la base de datos de trabajos"



class ProductoAdicionalInline(admin.TabularInline):
    model = Producto
    extra = 0  # Número de formularios adicionales vacíos a mostrar


# Registra la acción en el admin del modelo Presupuesto
class PresupuestoAdmin(admin.ModelAdmin):
    inlines = [ProductoAdicionalInline]
    list_display = ('empresa', 'nombre_trabajo', 'usuario', 'total_valores_productos', 'fecha_emision', 'aprobado')
    search_fields = ('empresa', 'nombre_trabajo')
    list_filter = ('aprobado', 'fecha_emision')
    actions = [duplicar_presupuesto]  # Agrega la acción personalizada

    # Personalizar la disposición de los campos en el formulario de administración
    fieldsets = (
        (None, {
            'fields': ('empresa', 'nombre_trabajo')
        }),
        ('Estado', {
            'fields': ('fecha_emision', 'fecha_ok', 'usuario', 'aprobado'),
        }),
    )

    def total_valores_productos(self, obj):
        total = obj.total_valores_productos()
        return f"{'$ '}{total}" 
    total_valores_productos.short_description = 'Valor Total'

if not admin.site.is_registered(Presupuesto):
    admin.site.register(Presupuesto, PresupuestoAdmin)
