from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
