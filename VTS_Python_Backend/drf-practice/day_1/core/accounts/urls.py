from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView,students

router = DefaultRouter()
router.register('user', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('students/',students,name='students')
]