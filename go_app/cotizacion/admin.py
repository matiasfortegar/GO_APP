from django.contrib import admin
from .models import Presupuesto, Producto

class ProductoAdicionalInline(admin.TabularInline):
    model = Producto
    extra = 1  # Número de formularios adicionales vacíos a mostrar

class PresupuestoAdmin(admin.ModelAdmin):
    inlines = [ProductoAdicionalInline]
    list_display = ('empresa', 'nombre_trabajo', 'fecha_emision', 'aprobado')
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

admin.site.register(Presupuesto, PresupuestoAdmin)