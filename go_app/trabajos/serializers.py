"""from rest_framework import serializers
from .models import OrdenTrabajo, ProductoOrden

class ProductoOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoOrden
        fields = '__all__'

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    productos = ProductoOrdenSerializer(many=True, read_only=True)

    class Meta:
        model = OrdenTrabajo
        fields = '__all__'"""