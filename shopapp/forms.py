from django import forms

from .models import *


class NameForm(forms.Form):
    class Meta:
        model = ProductPhoto
        fields = '__all__'