from django import forms
from django.forms.widgets import ClearableFileInput

from .models import *
from django.forms.models import inlineformset_factory
from django.core.validators import FileExtensionValidator


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
       




class ProductImageForm(forms.ModelForm):
    # image = forms.ImageField(widget=ClearableFileInput(attrs={'accept': 'image/*', 'placeholder': 'Select an image file'}),required=True, error_messages={'required': 'Please select an image file'})
    image = forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
    class Meta:
        model = ProductImage
        fields = ['image']


class LikeForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance.pk:
    #         self.fields['images'].queryset = self.instance.productimage_set.all()




    # images = forms.ModelMultipleChoiceField(
    #     queryset=ProductImage.objects.none(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False,
    # )

    # class Meta:
    #     model = Product
    #     # fields = '__all__'
    #     fields = ['ad_title', 'category', 'images']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance.pk:
    #         self.fields['images'].queryset = self.instance.productimage_set.all()