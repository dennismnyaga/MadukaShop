import random
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
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




@api_view(['POST'])
def register_user(request):
  
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    phone_number = request.data.get('phone_number')

    if not email or not password or not first_name or not last_name or not phone_number:
        return Response({'error': 'Please provide all required fields.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        verified_email = VerifiedEmail.objects.get(email=email, is_email_verified=True)
        print('verified_email:', verified_email)
    except VerifiedEmail.DoesNotExist:
        print('error')
        return Response({'error':'require email verification'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        print('fff')
        user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)
    except Exception as e:
        print('this is e ', e)
        return Response({'error':'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)



def password_reset(request):
    pass



@api_view(['POST'])
def send_otp(request):
    if request.method == "POST": 
        email = request.data.get('email')
        try:
            if CustomUser.objects.filter(email=email).exists():
                return Response({'message': 'Email already exists, try to login.'}, status=status.HTTP_400_BAD_REQUEST)
            
            if VerifiedEmail.objects.filter(email=email).exists():
                existing_entry = VerifiedEmail.objects.get(email=email)
                otp_number = random.randint(1000,9999)
                existing_entry.otp_number = otp_number
                existing_entry.save()

                # Send email
                subject = "Your email needs to be verified"
                message = f"Your verification code is {otp_number}"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email] 
                num_sent = send_mail(subject, message, email_from, recipient_list)

                if num_sent >= 1:
                    return Response({'message': 'An OTP code has been sent to your email.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Failed! Get OTP again!.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                subject = "Your email needs to be verified"
                otp_number = random.randint(1000,9999)
                message = f"Your verification code is {otp_number}"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email] 
                num_sent = send_mail(subject, message, email_from, recipient_list)
                if num_sent >= 1:
                    request.data['otp_number'] = otp_number
                    serializer = OtpSerializer(data=request.data, context={'request': request})
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response({'message': 'An otp code has been sent to your email.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Failed! Get otp again!.'}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    
@api_view(['POST'])
def verifyOtp(request):
    if request.method == "POST": 
        email = request.data.get('email')
        otp_number = request.data.get('otp_number')

        # Check if the email exists in the VerifiedEmail model
        verified_email = get_object_or_404(VerifiedEmail, email=email)
        
        

        # Check if the provided otp_number matches the email's otp_number
        if verified_email.otp_number == otp_number:
            # Check if the otp is not expired (timeout is not exceeded)
            current_time = timezone.now()
            creation_time = verified_email.timeout
            if current_time - creation_time <= timedelta(minutes=5):
                verified_email.is_email_verified = True
                verified_email.save() 
                return Response({'message': 'OTP verification successful.'}, status=status.HTTP_200_OK)
            else:
                
                return Response({'message': 'OTP code has expired, request a new one.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Invalid OTP code.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)