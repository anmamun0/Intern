from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet
from rest_framework.authtoken import views as drf_auth_views

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')
from rest_framework.authtoken import views

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', drf_auth_views.obtain_auth_token, name='api_token_auth'),

    path('api/auth/', views.obtain_auth_token),  # Token login endpoint
]
