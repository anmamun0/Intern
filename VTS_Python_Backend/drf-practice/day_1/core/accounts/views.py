from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializers,StudentSerializer
from .models import CustomUser
from rest_framework import viewsets
from django.contrib.auth import get_user_model
User = get_user_model()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()

    input_data = {'id': 2, 'name': 'Rahim', 'age': 20}


    serializer = StudentSerializer(data=input_data)
    if serializer.is_valid():
        print("This is data ->",serializer.data)
        print("This is ->",serializer.validated_data)
    else:
        print(serializer.errors)