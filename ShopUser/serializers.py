from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



class OtpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VerifiedEmail
        fields = "__all__"
        
        
class OtpUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['otp_number'] 