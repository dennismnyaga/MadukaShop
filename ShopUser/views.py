from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['first_name'] = user.first_name
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET','PUT'])
def apiuserhome(request, user_id=None):
    if request.method == 'GET':
        if user_id is not None:
            try:
                user = CustomUser.objects.get(id=user_id)
                serializer = UserSerializer(user, many=True)
                return Response(serializer.data)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        else:
            users = CustomUser.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
    elif request.method == 'PUT':
        user_id = request.data.get('user_id')
        is_active = request.data.get('is_active')
        print(f"is active status is {is_active}")
        try:
            user = CustomUser.objects.get(id=user_id)
            user.is_active = is_active
            user.save()
            return Response({'message':'User verification updated successfully'})
        except User.DoesNotExist:
            return Response({'error':'User not found'}, status=404)
    else:
        return Response({"error":"Invalid request method"}, status=405)






# @api_view(['GET', 'PUT'])
# def apidashShop(request, shop_id=None):
#     if request.method == 'GET':
#         if shop_id is not None:
#             try:
#                 shop = Shop.objects.get(id=shop_id)
#                 serializer = ShopSerializer(shop)
#                 return Response(serializer.data)
#             except Shop.DoesNotExist:
#                 return Response({'error': 'Shop not found'}, status=404)
#         else:
#             shop = Shop.objects.all()
#             serializer = ShopSerializer(shop, many=True)
#             return Response(serializer.data)
#     elif request.method == 'PUT':
#         shop_id = request.data.get('shop_id')
#         is_verified = request.data.get('is_verified')
#         try:
#             shop = Shop.objects.get(id=shop_id)
#             shop.is_verified = is_verified
#             shop.save()
#             return Response({'message':'User verification updated successfully'})
#         except Shop.DoesNotExist:
#             return Response({'error':'User not found'}, status=404)
#     else:
#         return Response({"error":"Invalid request methos"}, status=405)


@api_view(['POST'])
def register_user(request):
    print("am called logout")
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    phone_number = request.data.get('phone_number')

    if not email or not password or not first_name or not last_name or not phone_number:
        return Response({'error': 'Please provide all required fields.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)
    except Exception as e:
        print(f'this is the error {e}')
        return Response({'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)