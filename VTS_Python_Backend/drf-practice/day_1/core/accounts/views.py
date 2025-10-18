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
from rest_framework import status

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
 
@api_view(['GET', 'POST','PUT'])
def students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True, context={'request':request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)