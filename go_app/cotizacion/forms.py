from django import forms
from .models import Presupuesto, Producto

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'