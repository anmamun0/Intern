# accounts/views.py (snippet)
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny,BasePermission, SAFE_METHODS
from .permissions import IsInGroup, HasCustomActionPermission, DjangoModelPermissionsOrReadOnly
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

from rest_framework.decorators import api_view, permission_classes 
from rest_framework.views import APIView
from .permissions import IsAuthenticatedReadOnly

 
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

 

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, HasCustomActionPermission])
    def publish(self, request, pk=None):
        product = self.get_object()
        # publishing logic here...
        return Response({'status': 'published'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, HasCustomActionPermission])
    def discount(self, request, pk=None):
        # discount logic...
        return Response({'status': 'discount applied'}, status=status.HTTP_200_OK)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissionsOrReadOnly]
    # optionally use group check on class:
    # group_name = 'Cashiers'
