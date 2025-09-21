from django.contrib import admin
from django.urls import path,include
from .views import apiRegisterView, RegisterView,Logout 
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# session 
from django.contrib.auth.views import LoginView,LogoutView


router = DefaultRouter()
router.register('api_register',apiRegisterView)

urlpatterns = [
    path('',include(router.urls)), 
    path('api/login/',obtain_auth_token,name='api_login'),
    path('api/logout/',Logout.as_view(),name='api_logout'), 

    #  session
    path('register/',RegisterView.as_view(),name="register"),
    path("login/",LoginView.as_view(template_name="login.html"),name="login"), 
    path("logout/",LogoutView.as_view(),name="logout"),

]

 