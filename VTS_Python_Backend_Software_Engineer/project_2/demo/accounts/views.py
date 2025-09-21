from django.shortcuts import render

# Create your views here.
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST

from django.contrib.auth.models import User 
from rest_framework.exceptions import PermissionDenied
 

 #  Session 
from django.shortcuts import render 
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView 
from django.contrib.auth import login
from .forms import RegisterForm 
from django.urls import reverse_lazy 


class apiRegisterView(ModelViewSet):  
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    def initial(self, request, *args, **kwargs):
        if request.method not in ['POST']:
            raise PermissionDenied("Not allow without post request")
        return super().initial(request, *args, **kwargs)


class Logout(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response({"message":"Logout success"},status=HTTP_400_BAD_REQUEST)
    



# Session  
class RegisterView(CreateView):
    model = User 
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('blogs_list')

    def form_valid(self, form):
        res = super().form_valid(form)
        login(self.request,self.object)
        return res
     