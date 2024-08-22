from django.contrib import admin
from .models import TrabPresupuesto, TrabProducto

@admin.register(TrabPresupuesto)
class TrabajoPresupuestoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'nombre_trabajo', 'usuario', 'fecha_emision')
    search_fields = ['nombre_trabajo']  # Añade campos para buscar fácilmente

    def get_queryset(self, request):
        # Sobrescribe el queryset para usar la base de datos 'trabajos_db'
        return super().get_queryset(request).using('trabajos_db')

    def save_model(self, request, obj, form, change):
        # Sobrescribe la función de guardar para usar 'trabajos_db'
        obj.save(using='trabajos_db')

    def delete_model(self, request, obj):
        # Sobrescribe la función de eliminar para usar 'trabajos_db'
        obj.delete(using='trabajos_db')

    def get_search_results(self, request, queryset, search_term):
        # Sobrescribe la búsqueda para usar 'trabajos_db'
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset.using('trabajos_db'), use_distinct
    
@admin.register(TrabProducto)
class TrabajoProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_producto', 'cantidad']  # Ajusta según los campos que quieras mostrar
    search_fields = ['nombre_producto']  # Añade campos para buscar fácilmente