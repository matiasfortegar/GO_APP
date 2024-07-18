from rest_framework import serializers
from .models import Presupuesto, Producto

class CotizacionProducto(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields = '__all__'

class CotizacionPresupuesto(serializers.ModelSerializer):
    class Meta: 
        model = Presupuesto
        fields = '__all__'