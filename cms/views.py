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
@api_view(['GET'])
def apidashboard(request):
    products = Product.objects.order_by('date_posted')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
