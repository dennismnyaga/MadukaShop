from django.shortcuts import render
from shopapp.models import *
from ShopUser.models import *
from shopapp.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
@api_view(['GET', 'PUT'])
def apidashboard(request, product_id=None):
    if request.method == 'GET':
        if product_id is not None:
            try:
                product = Product.objects.get(id=product_id)
                serializer = ProductSerializer(product)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=404)
        else:
            products = Product.objects.order_by('-date_posted')
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
    elif request.method == 'PUT':
        product_id = request.data.get('product_id')
        dt = request.data
        print(f'This is the product id {product_id}')
        is_verified = request.data.get('is_verified')
        print(f'Is verified status is {is_verified}')
        try:
            product = Product.objects.get(id=product_id)
            product.is_verified = is_verified
            product.save()
            return Response({'message':'Product verification updated successfully'})
        except Product.DoesNotExist:
            return Response({'error':'Product not found'}, status=404)
    else:
        return Response({"error":"Invalid request methos"}, status=405)




@api_view(['GET', 'PUT'])
def apidashShop(request, shop_id=None):
    if request.method == 'GET':
        if shop_id is not None:
            try:
                shop = Shop.objects.get(id=shop_id)
                serializer = ShopSerializer(shop)
                return Response(serializer.data)
            except Shop.DoesNotExist:
                return Response({'error': 'Shop not found'}, status=404)
        else:
            shop = Shop.objects.all()
            serializer = ShopSerializer(shop, many=True)
            return Response(serializer.data)
    elif request.method == 'PUT':
        shop_id = request.data.get('shop_id')
        is_verified = request.data.get('is_verified')
        try:
            shop = Shop.objects.get(id=shop_id)
            shop.is_verified = is_verified
            shop.save()
            return Response({'message':'Shop verification updated successfully'})
        except Shop.DoesNotExist:
            return Response({'error':'Shop not found'}, status=404)
    else:
        return Response({"error":"Invalid request methos"}, status=405)




@api_view(['GET', 'PUT', 'DELETE'])
def apiproductdetails(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        product.update_views()
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def apidashCategory(request):
    category = ProductCategory.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apidashCategoryProducts(request, pk):
    try:
        productCategory = ProductCategory.objects.get(pk=pk)
        productsInCategory = Product.objects.filter(category=productCategory)
        serializer = ProductCategorySerializer(productsInCategory, many=True)
        return Response(serializer.data)
    except ProductCategory.DoesNotExist:
        return Response(status=404)


@api_view(['GET'])
def apidashLocation(request):
    location = Location.objects.all()
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)





@api_view(['GET'])
def apidashNewsLetter(request):
    letters = NewsLetterEmails.objects.all()
    serializer = NewsLetterEmailsSerializer(letters, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apidashshopdetails(request, pk):
    shop = Shop.objects.get(id=pk)
    serializer = ShopSerializer(shop, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def apidashShopCategory(request):
    shopcategory = ShopCategory.objects.all()
    serializer = ShopCategorySerializer(shopcategory, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apidashLike(request, pk):
    likes = Like.objects.filter(product__pk=pk)
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def newsletter_dashemails(request):
    serializer = NewsLetterEmailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def product_dashsearch(request):
    ad_title = request.query_params.get('ad_title')
    location = request.query_params.get('location')

    if ad_title is not None and location is not None:
        products = Product.objects.filter(ad_title__icontains=ad_title, location__name__icontains=location)
    elif ad_title is not None:
        products = Product.objects.filter(ad_title__icontains=ad_title)
    elif location is not None:
        products = Product.objects.filter(location__name__icontains=location)
    else:
        products = Product.objects.none()

    if products.exists():
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No such product found in our database'}, status=status.HTTP_404_NOT_FOUND)
