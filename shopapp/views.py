from django.shortcuts import render,  redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse

from .models import *

# Create your views here.

def home(request):
    products = Product.objects.all()
    print(products)
    context = {'products':products}
    return render(request, 'shopapp/home.html', context)



def details(request):
    context = {}
    return render(request, 'shopapp/details.html', context)



def add(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        # if data['category'] != 'none':
        #     category = Category.objects.get(id=data['category'])
        # elif data['category_new'] != '':
        #     category, created = Category.objects.get_or_create(
        #         name=data['category_new'])
        # else:
        #     category = None
        # ===================================
        product, created = Product.objects.get_or_create(
                # poster=request.user,
                name = request.POST['name'],
                price = request.POST['price'],
                condition = request.POST['condition'],
                description=request.POST['description'],
                category = request.POST['category']
                
                # expected_sales_date = request.POST['expected_sales_date'],
                
            )
        # ===================================

        for image in images:
            photo = Photo.objects.create(
                product = product,
                image=image,
            )

        return redirect('/')
    
    context = {}
    return render(request, 'shopapp/add.html', context)


def multistepform(request):
    categories = ProductCategory.objects.all()
    locations = Location.objects.all()
    shop = Shop.objects.all()
    shopcategory = ShopCategory.objects.all()

    if request.method == 'POST':
        data = request.POST
        if data['shop'] != 'none':
            shop = Shop.objects.get(id=data['shop'])
        elif data['shop_new'] != '':
            shopimages = request.FILES.getlist('shop_images')
            shop, created = Shop.objects.get_or_create(
                name=data['shop_new'],
                category = ProductCategory.objects.get(id=data['category']),
                # location = Location.objects.get(id=data['shoplocation']),
                description = data['des_new']
                )
            for image in shopimages:
                Shopphoto = ShopPhoto.objects.create(
                    shop=shop,
                    image = image
                )
        
        else:
            shop = None
        
        category = ProductCategory.objects.get(id=data['category'])
        location = Location.objects.get(id=data['location'])
        
        ad_title=data["ad_title"]
        # ad_condition=request.POST("ad_condition")
        price= data["ad_price"]
        description= data["ad_description"]
        # shop= data("shop")
        images = request.FILES.getlist('images')
        
        
        product, created = Product.objects.get_or_create(
            ad_title = ad_title,
            category = category,
            location = location,
            shop=shop,
            description = description,
            price = price,
        )


        for image in images:
            photo = ProductPhoto.objects.create(
                product = product,
                image=image,
            )

        messages.success(request,"Data Save Successfully")
        return redirect('/')
    context = {'categories':categories, 'locations':locations, 'shop':shop, 'shopcategory':shopcategory}
    return render(request,"shopapp/multistepform.html", context)






def about(request):
    context = {}
    return render(request, 'shopapp/about.html', context)






# import  rembg import remove