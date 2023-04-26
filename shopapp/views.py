from django.shortcuts import render,  redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.db.models import Count
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import *
from .forms import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def apihome(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)




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



@api_view(['POST'])
def apiproductlike(request, pk):
    print(f"This is the like data:  {request.body}")
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user_id = request.data.get('user_id')
    if user_id:
        like, created = Like.objects.get_or_create(product=product, user_id=user_id)
        if created:
            return Response({'message': 'Like added successfully!'})
        else:
            return Response({'message': 'You have already liked this product!'})
    else:
        return Response({'message': 'User ID is required!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def apiproductunlike(request, pk):
    print(f"This is the unlike data:  {request.body}")
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        like = Like.objects.get(product=product, user_id=user_id)
        like.delete()
        return Response({'message': 'Like removed successfully!'})
    except Like.DoesNotExist:
        return Response({'message': 'You have not liked this product!'}, status=status.HTTP_400_BAD_REQUEST)



        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_productApi(request):
    if request.method == 'POST':
        print(f"This is the response data: {request.data}")
        serializer = AddProductSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            images = request.FILES.getlist('images')
            serializer.save(owner=request.user, images=images)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


create_productApi.parsers = [MultiPartParser(), FormParser()]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_shopApi(request):
    if request.method == 'POST':
        serializer = AddShopSerializer(
            data=request.data, context={'request': request})
        print(request.data)
        if serializer.is_valid():
            shopimages = request.FILES.getlist('shopimages')
            serializer.save(owner=request.user, shopimages=shopimages)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            error_msg = f"Validation error: {serializer.errors}"
            print(error_msg)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


create_shopApi.parsers = [MultiPartParser(), FormParser()]


@api_view(['GET'])
def apiCategory(request):
    category = ProductCategory.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiCategoryProducts(request, pk):
    try:
        productCategory = ProductCategory.objects.get(pk=pk)
        productsInCategory = Product.objects.filter(category=productCategory)
        serializer = ProductCategorySerializer(productsInCategory, many=True)
        return Response(serializer.data)
    except ProductCategory.DoesNotExist:
        return Response(status=404)


@api_view(['GET'])
def apiLocation(request):
    location = Location.objects.all()
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiShop(request):
    shop = Shop.objects.all()
    serializer = ShopSerializer(shop, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apishopdetails(request, pk):
    shop = Shop.objects.get(id=pk)
    serializer = ShopSerializer(shop, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def apiShopCategory(request):
    shopcategory = ShopCategory.objects.all()
    serializer = ShopCategorySerializer(shopcategory, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def apiLike(request, pk):
    likes = Like.objects.filter(product__pk=pk)
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def newsletter_emails(request):
    serializer = NewsLetterEmailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def product_search(request):
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
        return Response("No such product found in our database")
