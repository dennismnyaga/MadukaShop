from django.urls import path
from .import views
from django.views.generic import TemplateView
from django.urls import re_path


app_name = 'shopapp'
urlpatterns = [

    # ==========apis==================================

    path('products/', views.apihome, name='products'),
    path('products/<str:pk>/', views.apiproductdetails, name='product_detail'),
    path('productcategory/', views.apiCategory, name='product_category'),
    path('location/', views.apiLocation, name='location'),
    path('shop/', views.apiShop, name='shop'),
    path('shop/<str:pk>/', views.apishopdetails, name='shop_detail'),
    path('shopcategory/', views.apiShopCategory, name='shop_category'),
    path('likes/<str:pk>/', views.apiLike, name='like'),
    path('createproductsapi/', views.create_productApi, name='create_product'),
    path('shopcreateapi/', views.create_shopApi, name='create_shop'),
    path('apicategoryproduct/<str:pk>/', views.apiCategoryProducts, name='category_product'),
    path('createnewsletter/', views.newsletter_emails, name='news_letter'),
    path('productsearch/', views.product_search, name='product_searchs'),
    path('productlike/<str:pk>/', views.apiproductlike, name='product_like'),
    path('productunlike/<str:pk>', views.apiproductunlike, name='product_unlike'),
    # re_path('.*', TemplateView.as_view(template_name='index.html')),
    
]
