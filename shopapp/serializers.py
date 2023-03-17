from rest_framework.serializers import ModelSerializer, ImageField, PrimaryKeyRelatedField, ListField
from . models import *
from rest_framework import serializers

class ShopImageSerializer(ModelSerializer):
    class Meta:
        model = ShopPhoto
        fields = ['id', 'image']


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']
        


class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    date_posted = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = '__all__'


# class AddProductImageSerializer(ModelSerializer):
#     image = serializers.ImageField(required=False)
    
#     class Meta:
#         model = ProductImage
#         fields = ('image')


# class AddProductSerializer(ModelSerializer):
#     image = AddProductImageSerializer(many=True)
#     owner = serializers.ReadOnlyField(source='owner.email')

#     class Meta:
#         model = Product
#         fields = '__all__'
#         read_only_fields = ('id', 'date_posted', 'likes', 'views', 'owner')

#     def create(self, validated_data):
#         images_data = self.context.get('view').request.FILES
#         images_serializer = self.fields['image']
#         product = Product.objects.create(**validated_data)


#         for image_data in images_data.values():
#             image = {'image': image_data}
#             serializer = images_serializer(data=image)

#             if serializer.is_valid():
#                 serializer.save(product=product)
#             else:
#                 raise serializer.errors

#         return product



class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    
    class Meta:
        model = ProductImage
        fields = ('id', 'image')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'ad_title', 'category', 'location', 'description', 'price',  'shop',  'images')

       

        

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        print(f"This are the images: {images_data}")
        product = Product.objects.create(**validated_data)
        print(f"Product created with id: {product.id}")
        for image_data in images_data:
            image_dict = {'image': image_data}
            product_image = ProductImage.objects.create(product=product,  **image_dict)
            print(f"Product image created with id: {product_image.id}")
        return product

       



class ShopSerializer(ModelSerializer):
    shopimages = ShopImageSerializer(many=True, read_only=True)
    class Meta:
        model = Shop
        fields = '__all__'



class CategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
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


# class ProductImageSerializer(ModelSerializer):
#     image = ListField(
#         child=ImageField(allow_empty_file=False, use_url=True),
#         required=True
#     )

#     class Meta:
#         model = ProductImage
#         fields = ('id', 'product', 'image')



# class ProductSerializer(ModelSerializer):
#     shop = PrimaryKeyRelatedField(queryset=Shop.objects.all())
#     location = PrimaryKeyRelatedField(queryset=Location.objects.all())
#     images = ProductImageSerializer(many=True)
#     class Meta:
#         model = Product
#         fields = ('id','ad_title','category','location','description','price','shop','images')
