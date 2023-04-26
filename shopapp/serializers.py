from rest_framework.serializers import ModelSerializer, ImageField, PrimaryKeyRelatedField, ListField
from . models import *
from rest_framework import serializers
from django.db import transaction
from django.db.models import Q


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


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

    class Meta:
        model = Product
        fields = ('id', 'ad_title', 'category', 'location',
                  'description', 'price',  'shop',  'images')

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        print(f"This are the images: {images_data}")
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
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = ShopPhoto
        fields = ('id', 'image')


class AddShopSerializer(serializers.ModelSerializer):
    shopimages = AddShopImageSerializer(many=True, required=False)

    class Meta:
        model = Shop
        fields = ('id', 'name', 'category', 'location',
                  'description', 'shopimages')

    def create(self, validated_data):
        images_data = validated_data.pop('shopimages', [])
        print(f"This is the images data {images_data}")
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


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
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