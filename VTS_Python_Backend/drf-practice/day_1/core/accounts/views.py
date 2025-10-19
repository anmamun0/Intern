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
 

# --------------------------------------------
# RESTView - Function Base  - Custom Create [GET,POST,PUT,PATCH,DELETE,HEAD]
# --------------------------------------------
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




# --------------------------------------------
# RESTView - APIView - Custom Create [GET,POST,PUT,PATCH,DELETE,HEAD]
# --------------------------------------------
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class StudentAPIView(APIView): 
    def get(self,request,pk=None):
        if pk is not None: 
            student = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
        qs = Student.objects.all()
        serializer = StudentSerializer(qs,many=True)
        return Response(serializer.data)
        
    # with pagination GET Request : Option
    def get(self, request, pk=None):
        page = int(request.query_params.get('page', 1))  
        limit = 5
        start = (page - 1) * limit
        end = page * limit

        students = Student.objects.all()[start:end]
        serializer = StudentSerializer(students, many=True)
        return Response({
            "page": page,
            "count": Student.objects.count(),
            "results": serializer.data
        })
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Student updated successfully", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Student partially updated", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        pass

# ----------------------------------------------------
# RESTView - Custom CRUD ViewSet - [list, retrieve, create, update,partial_update, delete]
# ----------------------------------------------------
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

class IsOwnerOfStudent(BasePermission):
    # Request → has_permission → (if True) → view method (list/retrieve/create...)
    # Request → has_permission → view method (retrieve/update/destroy) → get_object → has_object_permission → action on object
    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            raise NotAuthenticated(detail={"error": "Login first"})

        if request.method in ['GET']:
            return True
        
        if obj.name != request.user.username:
            raise PermissionDenied(detail={"error": "You are not the owner of this student"})
        return True

class StudentViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOfStudent]
    # /students/  >> return will all data
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    # Custom Action
    @action(detail=False, methods=['get'])
    def top_students(self, request):
        students = Student.objects.filter(age__gte=20)[:1]
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    # retrieve()  >> /students/<id>/ return will selected data
    def retrieve(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        self.check_object_permissions(request, student)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
 
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def update(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        self.check_object_permissions(request, student)
        
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def partial_update(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        self.check_object_permissions(request, student)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def destroy(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        self.check_object_permissions(request, student)
        student.delete()
        return Response({'msg': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT) 
        

from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
# --------------------------------------------
# RESTView - ModelViewSet - Auto Maintain [GET,POST,PUT,PATCH,DELETE,HEAD] and Auto Create url endpoint
# ModelSerializer + queryset + CRUD method all auto built-in 
# --------------------------------------------
 
class StudentModelView(ModelViewSet):
    pass 



