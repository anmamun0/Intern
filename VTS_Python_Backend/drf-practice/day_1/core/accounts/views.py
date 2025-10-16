from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializers
from .models import CustomUser
from rest_framework import viewsets
from django.contrib.auth import get_user_model
User = get_user_model()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()


