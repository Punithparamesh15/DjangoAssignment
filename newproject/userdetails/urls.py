from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', home, name='home'),
    path('api/users/', UserAPIView.as_view(), name='user-list'), 
    path('api/users/<int:user_id>/', UserAPIView.as_view(), name='user-detail'),
    path('api/admins/', AdminAPIView.as_view(), name='admin-list'),
    path('api/admins/<uuid:admin_id>/', AdminAPIView.as_view(), name='admin-detail'),
    # path('api/login/', UserLoginAPIView.as_view(), name='user-login'),
    # path('api/login/', obtain_auth_token, name='api-login')             #Token login endpoint
    path('api/login/', UserLoginAPIView.as_view(), name='user-login'),  # JWT login endpoint
]