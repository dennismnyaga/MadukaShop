from django.urls import path
from .import views


app_name = 'shopusers'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.log, name = 'log'),
]
