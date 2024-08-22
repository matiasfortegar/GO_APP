from rest_framework import serializers
from .models import TrabPresupuesto, TrabProducto

class TrabajopresupuestoSerial(serializers.ModelSerializer):
    class Meta: 
        model = TrabPresupuesto
        fields = '__all__'

class TrabajoproductoSerial(serializers.ModelSerializer):
    class Meta: 
        model = TrabProducto
        fields = '__all__'