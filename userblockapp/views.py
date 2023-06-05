from django.utils import timezone
from rest_framework.decorators import api_view
from userblockapp.serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework import status
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@api_view(['POST'])
def register_view(request):
    dataall = request.data
    dataall['password']=pwd_context.hash(dataall['password'])
    serializer = UserSerializer(data=dataall)
    # print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200)
    

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        dataall = request.data
        email = dataall['email']
        password = dataall['password']
        email = User.objects.filter(email=email)
        user_count = 0
        if email :  
            if email[0].user_count < 5:
                if(pwd_context.verify(hash=email[0].password,secret=password)): 
                    return Response("login successfully!!")
                else:
                    email[0].user_count += 1
                    email[0].save()
                    if email[0].user_count == 5:
                        email[0].block = False
                        email[0].expiredAt = timezone.now() + timezone.timedelta(minutes=3)
                        email[0].save()
                        return Response("Your account has been blocked for 3 minutes.")
                    return Response("Invalid password!") 
            else:
                if email[0].user_count == 5:
                    if email[0].expiredAt > timezone.now():
                        return Response(f"Please Try Again Login After {email[0].expiredAt-timezone.now()} Seconds!")
                    else:
                        email[0].block = True
                        email[0].user_count = 0
                        email[0].save()
                        return Response("Please Login Again! Unblock User!")
        return Response("Email verification failed!")




























































































































































































































































# @api_view(['POST'])
# def login_view(request):
#     if request.method == 'POST':
#         dataall = request.data
#         email = dataall['email']
#         password = dataall['password']
#         email = User.objects.filter(email=email)
#         user_count = 0
#         if email :  
#             if email[0].user_count < 5:
#                 if(pwd_context.verify(hash=email[0].password,secret=password)): 
#                     return Response("login successfully!")
#                 else:
#                     email[0].user_count += 1
#                     email[0].save()
#                     if email[0].user_count == 5:
#                         email[0].block = False
#                         email[0].expiredAt = timezone.now() + timezone.timedelta(minutes=3)
#                         email[0].save()
#                         return Response("Your account has been blocked for 3 minutes.")
#                     return Response("Invalid password!")
#             else:    
#                 if email[0].user_count == 5:
#                     expiredAt = User.objects.filter(expiredAt = email[0].expiredAt).values().last()   
#                     if expiredAt['expiredAt']:
#                         if email[0].expiredAt < timezone.now():
#                             email[0].user_count = 0
#                             email[0].block = True
#                             email[0].expiredAt 
#                             email[0].save()
#                             return Response("Login Again! Unblock User!")
#                         return Response(f"Please Try Again Login After {email[0].expiredAt-timezone.now()} Minutes!")
            
#         return Response("Email verification failed!")






















































