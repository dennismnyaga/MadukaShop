from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    context = {}
    return render(request, 'ShopUser/home.html', context)




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('shopapp:home')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    
    context = {'form':form}
    return render(request, 'ShopUser/log.html', context)


# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.name = form.cleaned_data.get('name')
#             user.first_name = form.cleaned_data.get('first_name')
#             user.last_name = form.cleaned_data.get('last_name')
#             user.email = form.cleaned_data.get('email')
#             user.phone = form.cleaned_data.get('phone')
#             user.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('shopapp:home')
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'ShopUser/register.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.profile_pic = form.cleaned_data['profile_pic']
            user.save()
            return redirect('shopusers:login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'ShopUser/register.html', context)