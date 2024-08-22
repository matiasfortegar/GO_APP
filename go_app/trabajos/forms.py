from django import forms
from .models import TrabPresupuesto, TrabProducto

class TrabajoPresupuestoForm(forms.ModelForm):
    class Meta:
        model = TrabPresupuesto
        fields = ['original_presupuesto', ]

class TrabajoProductoForm(forms.ModelForm):
    class Meta:
        model = TrabProducto
        fields = [
            'nombre_producto', 'cantidad', 'cantidad_pliego', 
            'medida_alto', 'medida_ancho', 'papel', 
            'terminacion', 'valor'
        ]
