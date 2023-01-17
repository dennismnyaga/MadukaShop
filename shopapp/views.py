from django.shortcuts import render,  redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .forms import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def apihome(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def apiproductdetails(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)
    

def home(request):

    products = Product.objects.prefetch_related('images').order_by('-date_posted')
    categories = ProductCategory.objects.annotate(num_products=Count('product'))
    context = {'products':products, 'categories':categories}

    return render(request, 'shopapp/home.html', context)


def shops(request):
    shops = Shop.objects.prefetch_related('shop_images').order_by('-registered_on')
    categories = ProductCategory.objects.annotate(num_products=Count('product'))
    context = {'shops':shops, 'categories':categories}
    return render(request, 'shopapp/shops.html', context)


def shop_details(request, shop_id):
    categories = ProductCategory.objects.annotate(num_products=Count('product'))

    shop = Shop.objects.get(id=shop_id)
    # images = ProductImage.objects.filter(product=product)


    context = {'categories':categories, 'shop':shop}
    return render(request, 'shopapp/shop_details.html', context)



def like(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = Product.objects.get(id=product_id)
        user = request.user
        existing_like = Like.objects.filter(user=user, product=product).first()
        if existing_like:
            existing_like.delete()
        else:
            Like.objects.create(user=user, product=product)
        
        return redirect('shopapp:home')


def view_category(request, category_id):
    category = get_object_or_404(ProductCategory, pk=category_id)
    product =  Product.objects.filter(category=category)
    products = product.prefetch_related('images').order_by('-date_posted')
    categories = ProductCategory.objects.annotate(num_products=Count('product'))
    # products =  Product.objects.prefetch_related('images').order_by('-date_posted').filter(category=category)
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'shopapp/category.html', context)


def detail_page(request, product_id):
    product = Product.objects.get(id=product_id)
    images = ProductImage.objects.filter(product=product)

    product.update_views()

    products = Product.objects.prefetch_related('images').all()
    context = {'product':product, 'images':images, 'products':products}

    return render(request, 'shopapp/details.html', context)

# @login_required
def create_product(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            for image in request.FILES.getlist('images'):
                ProductImage.objects.create(product=product, image=image)
            return redirect('shopapp:home')
            # return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm()
    context = {'products': products, 'form': form}
    return render(request, 'shopapp/create_product.html', context)


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
        # if data['shop'] != 'none':
        shop = Shop.objects.get(id=data['shop'])
        # elif data['shop_new'] != '':
            # shopimages = request.FILES.getlist('shop_images')
            # shop, created = Shop.objects.get_or_create(
                # name=data['shop_new'],
                # category = ProductCategory.objects.get(id=data['category']),
                # location = Location.objects.get(id=data['shoplocation']),
                # description = data['des_new']
        #         )
        #     for image in shopimages:
        #         Shopphoto = ShopPhoto.objects.create(
        #             shop=shop,
        #             image = image
        #         )
        
        # else:
        #     shop = None
        
        category = ProductCategory.objects.get(id=data['category'])
        location = Location.objects.get(id=data['location'])
        
        ad_title=data["ad_title"]
        # ad_condition=request.POST("ad_condition")
        price= data["ad_price"]
        description= data["ad_description"]
        # shop= data("shop")
        images = request.FILES.getlist('images')
        owner = request.user
        
        
        product, created = Product.objects.get_or_create(
            ad_title = ad_title,
            category = category,
            location = location,
            shop=shop,
            description = description,
            price = price,
            owner=owner,
        )


        for image in images:
            photo = ProductImage.objects.create(
                product = product,
                image=image,
            )

        messages.success(request,"Data Save Successfully")
        return redirect('/')
    context = {'categories':categories, 'locations':locations, 'shop':shop, 'shopcategory':shopcategory}
    return render(request,"shopapp/multistepform.html", context)

def addshop(request):
    categories = ProductCategory.objects.all()
    locations = Location.objects.all()
    shop = Shop.objects.all()
    shopcategory = ShopCategory.objects.all()

    if request.method == 'POST':
        data = request.POST
        shopimages = request.FILES.getlist('shop_images')
        shop, created = Shop.objects.get_or_create(
            name=data['shop_name'],
            category = ShopCategory.objects.get(id=data['category']),
            location = Location.objects.get(id=data['shoplocation']),
            description = data['des_new'],
            owner = request.user,
            )
        for image in shopimages:
            Shopphoto = ShopPhoto.objects.create(
                shop=shop,
                image = image
            )
        messages.success(request,"Shop has been created Successfuly")
        return redirect('shopapp:home')
    context = {'categories':categories, 'locations':locations, 'shop':shop, 'shopcategory':shopcategory}
    return render(request,"shopapp/createshop.html", context)




def about(request):
    context = {}
    return render(request, 'shopapp/about.html', context)






# import  rembg import remove