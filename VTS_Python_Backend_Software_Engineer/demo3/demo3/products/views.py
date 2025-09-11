from django.shortcuts import render

# Create your views here.
from .serializers import Category, Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # GET: anyone, POST/PUT/DELETE: authenticated only
    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]



class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer