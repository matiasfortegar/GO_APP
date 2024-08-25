from django import forms
from .models import OrdenTrabajo, ProductoOrden

class TrabajoPresupuestoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'

class TrabajoProductoForm(forms.ModelForm):
    class Meta:
        model = ProductoOrden
        fields = '__all__'