from django.urls import path,include
from .views import RegisterView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
0

router = DefaultRouter()
router.register('register',RegisterView)

urlpatterns = [
    path('',include(router.urls)),
    path('login/',obtain_auth_token,name="login"),
]