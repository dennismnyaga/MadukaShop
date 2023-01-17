from rest_framework.serializers import ModelSerializer
from . models import *


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image',)

class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'