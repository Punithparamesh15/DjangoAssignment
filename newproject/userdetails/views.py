from pkgutil import get_data
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import UserSerializer, AdminSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated, AllowAny
from oauth2_provider.views import TokenView
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.models import Application

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the new project!")

class UserAPIView(APIView):
    def get(self, request, user_id=None):
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print("Validated Data:", validated_data) 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                print("Validated Data:", validated_data) 
                serializer.save()
                return Response(serializer.data)
            else:
                print("Errors:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, data=request.data, partial=True)  # Allow partial updates
            if serializer.is_valid():
                validated_data = serializer.validated_data
                print("Validated Data:", validated_data) 
                serializer.save()
                return Response(serializer.data)
            else:
                print("Errors:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class AdminAPIView(APIView):
    def get(self, request, admin_id=None):
        if admin_id:
            try:
                admin = Admin.objects.get(id=admin_id)
                serializer = AdminSerializer(admin)
                return Response(serializer.data)
            except Admin.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
            serializer = AdminSerializer(admin, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
            serializer = AdminSerializer(admin, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
            admin.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

#Token Authentication
"""class TokenLoginView(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated access for login

    def post(self, request):
        contact = request.data.get('contact')
        password = request.data.get('password')

        if not contact or not password:
            return Response({"error": "Both contact and password are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(contact=contact)
            if check_password(password, user.password):
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)"""

# JWT Authentication View
"""class JWTLoginView(APIView):

    permission_classes = [AllowAny] 

    def post(self, request):
        contact = request.data.get('contact')
        password = request.data.get('password')

        if not contact or not password:
            return Response({"error": "Both contact and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(contact=contact)
            
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({
                    'access': access_token,
                    'refresh': str(refresh),
                    }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)"""
        
class UserDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user                   # Retrieve the authenticated user from the token

        try:
            user_serializer = UserSerializer(user)
            admin = Admin.objects.get(user=user)  # Get the associated admin info
            admin_serializer = AdminSerializer(admin)

            return Response({
                "admin": admin_serializer.data
            })
        except Admin.DoesNotExist:
            return Response({"error": "Admin details not found."}, status=status.HTTP_404_NOT_FOUND)
        
# Knox Authentication View
"""class KnoxLoginView(KnoxLoginView):
    def post(self, request, *args, **kwargs):
        contact = request.data.get('contact')
        password = request.data.get('password')

        if not contact or not password:
            return Response({"error": "Both contact and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(contact=contact)
            
            if user.check_password(password):
                token = self.get_tokens_for_user(user)
                return Response({'token': token[0]}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)"""
        
"""class UserLoginAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        contact = request.data.get('contact')
        password = request.data.get('password')

        try:
            user = User.objects.get(contact=contact)
            
            if check_password(password, user.password):

                # Generate JWT Token
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                
                user_data = UserSerializer(user).data
                return Response({
                    "access_token": str(access_token),              # Access token for authentication
                    "user": user_data
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid password."}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)"""

"""class UserDetailsAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, user_id=None):
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                if user != request.user:              # Check if user is authenticated by token
                    return Response({"error": "You are not authorized to access this data."}, status=status.HTTP_403_FORBIDDEN)
                user_serializer = UserSerializer(user)
                admin = Admin.objects.get(user=user)  # Get the admin info
                admin_serializer = AdminSerializer(admin)
                return Response({
                    "user": user_serializer.data,
                    "admin": admin_serializer.data
                })
            except (User.DoesNotExist, Admin.DoesNotExist):
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)"""
        
