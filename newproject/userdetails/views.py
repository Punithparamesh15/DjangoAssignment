from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import UserSerializer, AdminSerializer
from django.contrib.auth.hashers import check_password, make_password

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
        
class UserLoginAPIView(APIView):
    def post(self, request):
        contact = request.data.get('contact')
        password = request.data.get('password')

        try:
            user = User.objects.get(contact=contact)
            if user.password == "":
                user.password = make_password(password)  
                user.save()  

            if check_password(password, user.password):
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid password."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user_data = {
                'contact': contact,
                'password': make_password(password), 
                **request.data
            }
            serializer = UserSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
