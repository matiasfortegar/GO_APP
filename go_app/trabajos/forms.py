from django import forms
from .models import OrdenTrabajo, ProductoOrden

class TrabajoPresupuestoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = ['presupuesto', ]

class TrabajoProductoForm(forms.ModelForm):
    class Meta:
        model = ProductoOrden
        fields = ['nombre_producto', 'cantidad', 'cantidad_pliego',
                  'medida_alto', 'medida_ancho', 'papel',
                  'terminacion', 'valor'
                  ]