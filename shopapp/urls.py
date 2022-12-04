from django.urls import path
from .import views


app_name = 'shopapp'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('details/', views.details, name = 'details'),
    path('add/', views.add, name = 'add'),
    path('about/', views.about, name = 'about'),


    path('multistepform/', views.multistepform, name='multistepform'),
    path('multistepform_save/', views.multistepform_save, name='multistepform_save'),
]
