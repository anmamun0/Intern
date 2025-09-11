from django.shortcuts import render
from .serializers import Register
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class RegisterView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Register
    # permission_classes = [IsAuthenticated]  # only logged-in users can access

    def initial(self, request, *args, **kwargs):
        if request.method not in ["GET","POST"]:
            raise PermissionDenied("PermissionDenied, Just GET and POST Allow !")
        return super().initial(request, *args, **kwargs)
 