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
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.ht)
    
    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH' 
        serializer = StudentSerializer(student, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

