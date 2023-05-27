from django.urls import path
from .import views
from .views import  MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


app_name = 'shopusers'
urlpatterns = [
    path('register/', views.register_user, name='users_regist'),
    path('users/', views.apiuserhome, name='users'),
    path('users/<str:user_id>/', views.apiuserhome, name='users'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
