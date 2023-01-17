from django.urls import path
from .import views


app_name = 'shopapp'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('shops/', views.shops, name = 'shops'),
    path('shop_detail/<shop_is>/', views.shop_details, name = 'shop_detail'),
    path('like/', views.like, name='like'),
    path('details/<product_id>/', views.detail_page, name = 'details'),
    # path('details/', views.details, name = 'details'),
    path('add/', views.add, name = 'add'),
    path('about/', views.about, name = 'about'),


    path('multistepform/', views.multistepform, name='multistepform'),
    # path('multistepform_save/', views.multistepform_save, name='multistepform_save'),
    path('create_product/', views.create_product, name='create_form'),
    path('create_shop/', views.addshop, name='create_shop'),
    path('category/<int:category_id>/', views.view_category, name='view_category'),
    # ==========apis==================================

    path('products/', views.apihome, name='products'),
    path('products/<str:pk>/', views.apiproductdetails, name='product_detail')
]
