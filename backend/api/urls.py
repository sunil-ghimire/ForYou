from django.urls import path, include
from rest_framework import routers

from .views import create_user
from users.models import CustomUser

router = routers.DefaultRouter()

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
]