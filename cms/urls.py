from django.urls import path
from .import views


app_name = 'cms'
urlpatterns = [
    # ==========apis==================================
    path('dashboard/', views.apidashboard, name='dashboard'),
    path('dashboard/<str:product_id>/', views.apidashboard, name='dashboard'),
    path('dashboardshops/', views.apidashShop, name='dashboardshop'),
    path('dashboardshops/<str:shop_id>/',views.apidashShop, name='dashboardshop'),
    path('products/<str:pk>/', views.apiproductdetails, name='product_detail'),
    path('newsletters/', views.apidashNewsLetter, name='Newsletter'),
    path('locations/', views.apidashLocation, name='location'),
]