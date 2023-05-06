from django.urls import path
from .import views


app_name = 'cms'
urlpatterns = [
    # ==========apis==================================
    path('dashboard/', views.apidashboard, name='dashboard'),
]
