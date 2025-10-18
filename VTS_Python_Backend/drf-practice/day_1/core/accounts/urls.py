from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView,students,student_detail

router = DefaultRouter()
router.register('user', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('students/',students,name='students'),
    path('students/<int:pk>/', student_detail),  

]