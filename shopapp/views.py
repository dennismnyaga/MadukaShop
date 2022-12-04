from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

from .models import *

# Create your views here.

def home(request):
    context = {}
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
    return render(request,"shopapp/multistepform.html")

def multistepform_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("shopapp:multistepform"))
    else:
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        phone=request.POST.get("phone")
        twitter=request.POST.get("twitter")
        facebook=request.POST.get("facebook")
        gplus=request.POST.get("gplus")
        email=request.POST.get("email")
        password=request.POST.get("pass")
        cpass=request.POST.get("cpass")
        if password!=cpass:
            messages.error(request,"Confirm Password Doesn't Match")
            return HttpResponseRedirect(reverse('shopapp:multistepform'))

        try:
            multistepform=MultiStepFormModel(fname=fname,lname=lname,phone=phone,twitter=twitter,facebook=facebook,gplus=gplus,email=email,password=password)
            multistepform.save()
            messages.success(request,"Data Save Successfully")
            return HttpResponseRedirect(reverse('multistepform'))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('shopapp:multistepform'))



def about(request):
    context = {}
    return render(request, 'shopapp/about.html', context)