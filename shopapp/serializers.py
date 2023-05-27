from rest_framework.serializers import ModelSerializer, ImageField, PrimaryKeyRelatedField, ListField
from . models import *
from rest_framework import serializers
from django.db import transaction
from django.db.models import Q


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'





class AddProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = ProductImage
        fields = ('id', 'image')


class AddProductSerializer(serializers.ModelSerializer):
    images = AddProductImageSerializer(many=True, required=False)
    # location = LocationSerializer(required=False)
    location = serializers.CharField()

    class Meta:
        model = Product
        fields = ('id', 'ad_title', 'category', 'location', 'description', 'price',  'shop',  'images')



    def create(self, validated_data):
        print(f"Validated Data {validated_data}")
        images_data = validated_data.pop('images', [])
        location_data = validated_data.pop('location', None)
        print(f"Location name is {location_data}")
        if location_data:
            location = Location.objects.filter(name=location_data).first()
            if not location:
                location = Location.objects.create(name = location_data)
            validated_data['location'] = location
      
        product = Product.objects.create(**validated_data)
        print(f"Product created with id: {product.id}")
        for image_data in images_data:
            image_dict = {'image': image_data}
            product_image = ProductImage.objects.create(
                product=product,  **image_dict)
            print(f"Product image created with id: {product_image.id}")
        return product


class ShopImageSerializer(ModelSerializer):
    class Meta:
        model = ShopPhoto
        fields = ['id', 'image']


class ShopSerializer(ModelSerializer):
    shopimages = ShopImageSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = '__all__'


class AddShopImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    

    class Meta:
        model = ShopPhoto
        fields = ('id', 'image')


class AddShopSerializer(serializers.ModelSerializer):
    shopimages = AddShopImageSerializer(many=True, required=False)
    location = serializers.CharField()

    class Meta:
        model = Shop
        fields = ('id', 'name', 'category', 'location',
                  'description', 'shopimages')

    def create(self, validated_data):
        images_data = validated_data.pop('shopimages', [])
        location_data = validated_data.pop('location', None)
        if location_data:
            location = Location.objects.filter(name=location_data).first()
            if not location:
                location = Location.objects.create(name = location_data)
            validated_data['location'] = location
        shop = Shop.objects.create(**validated_data)
        for image_data in images_data:
            image_dict = {'image': image_data}
            shop_image = ShopPhoto.objects.create(shop=shop,  **image_dict)
        return shop





class CategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'





class ShopCategorySerializer(ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = '__all__'


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class NewsLetterEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetterEmails
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        email = validated_data.get('email')
        if NewsLetterEmails.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        else:
            instance = NewsLetterEmails.objects.create(**validated_data)
            return instance



# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'