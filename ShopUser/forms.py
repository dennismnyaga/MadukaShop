from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from phonenumber_field.formfields import PhoneNumberField

from .models import *



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    profile_pic = forms.ImageField()
    phone_number = PhoneNumberField(required=True, region='KE', help_text='Required. Enter a valid US phone number.')
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2', 'profile_pic']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            self.add_error('password2', "Passwords do not match")
        return cleaned_data
            

    def clean_username(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            
            raise forms.ValidationError('A user with that email already exists.')
        return email