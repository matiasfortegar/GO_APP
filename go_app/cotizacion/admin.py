from django.contrib import admin
from .models import Presupuesto, Producto

# Register your models here.


class ProductoAdicionalInline(admin.TabularInline):
    model = Producto
    extra = 0  # Número de formularios adicionales vacíos a mostrar



class PresupuestoAdmin(admin.ModelAdmin):
    inlines = [ProductoAdicionalInline]
    list_display = ('empresa', 'nombre_trabajo', 'usuario', 'total_valores_productos', 'fecha_emision', 'aprobado')
    search_fields = ('empresa', 'nombre_trabajo')
    list_filter = ('aprobado', 'fecha_emision')

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

admin.site.register(Presupuesto, PresupuestoAdmin)
