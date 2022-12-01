from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'ShopUser/home.html', context)



def log(request):
    context = {}
    return render(request, 'ShopUser/log.html', context)