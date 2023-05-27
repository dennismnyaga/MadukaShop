from shopapp.models import *
from rest_framework.serializers import ModelSerializer, ImageField, PrimaryKeyRelatedField, ListField
from rest_framework import serializers



class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model = NewsLetterEmails
        fields = '__all__'