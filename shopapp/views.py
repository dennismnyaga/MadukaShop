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


@api_view(['GET'])
def apiproductdetails(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_productApi(request):
    if request.method == 'POST':
        print(f"This is the response data: {request.data}")
        serializer = AddProductSerializer(data=request.data, context={'request': request})
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
        serializer = AddShopSerializer(data=request.data, context={'request': request})
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
def apiLike(request):
    likes = Like.objects.all()
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)







