# SE ENCARGA DE CONVERTIR LOS DATOS
from .models import *
from rest_framework import serializers


class TipoProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'


class ProductoSerializers(serializers.ModelSerializer):
    #AGREGAMOS LA FK
    tipo = TipoProductoSerializers(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'


# SERIALIZER - VIEWSET - URL