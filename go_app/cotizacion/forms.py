from django import forms
from .models import Presupuesto, Producto

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['empresa', 'nombre_trabajo', 'aprobado']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre_producto', 'cantidad', 'cantidad_pliego', 
            'medida_alto', 'medida_ancho', 'papel', 
            'terminacion', 'valor'
        ]
