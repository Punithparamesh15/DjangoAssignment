from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('api/users/', UserAPIView.as_view(), name='user-list'), 
    path('api/users/<int:user_id>/', UserAPIView.as_view(), name='user-detail'),
    path('api/admins/', AdminAPIView.as_view(), name='admin-list'),
    path('api/admins/<uuid:admin_id>/', AdminAPIView.as_view(), name='admin-detail'),
]