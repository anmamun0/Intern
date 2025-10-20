from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView,students,student_detail,StudentAPIView,StudentViewSet,StudentModelView
 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView
)
jwt_login_urls = [
    path('api/token/',TokenObtainPairView.as_view(),name="api_token"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
]


router = DefaultRouter()
router.register('user', UserView, basename='user')
router.register('students-viewset', StudentViewSet, basename='students')
router.register('students-model-viewset', StudentModelView, basename='students-model-viewset')
 
urlpatterns = (
    [
        path('', include(router.urls)),
        path('students/',students,name='students'),
        path('students/<int:pk>/', student_detail),  
        path('api/student/',StudentAPIView.as_view(),name="studentapi"),
        path('api/student/<int:pk>/', StudentAPIView.as_view(), name='student-detail'),  
    ]   + jwt_login_urls   
)

