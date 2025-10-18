from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializers,StudentSerializer
from .models import CustomUser
from rest_framework import viewsets
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
 

@api_view(['GET'])
def students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True,context={'request':request})
    print("This is data ->", serializer.data)
    return Response(serializer.data)