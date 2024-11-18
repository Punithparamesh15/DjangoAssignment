from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('api/users/', UserAPIView.as_view(), name='user-list'), 
    path('api/users/<int:user_id>/', UserAPIView.as_view(), name='user-detail'),
    path('api/admins/', AdminAPIView.as_view(), name='admin-list'),
    path('api/admins/<uuid:admin_id>/', AdminAPIView.as_view(), name='admin-detail'),

    #path('api/token/login/', TokenLoginView.as_view(), name='login'),              # Token login

    #path('api/jwt/login/', JWTLoginView.as_view(), name='jwt-login'),              # JWT login endpoint
    path('api/user/details/', UserDetailsAPIView.as_view(), name='user-details'),  # Protected user details endpoint
]