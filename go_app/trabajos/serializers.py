from rest_framework import serializers
from .models import OrdenTrabajo

class OrdenTrabajoSerial(serializers.ModelSerializer):
    class Meta: 
        model = OrdenTrabajo
        fields = '__all__'