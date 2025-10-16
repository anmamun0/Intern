from django.urls import path,include
from .views import register_view,login_user,profile_view,logout_user,home_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',home_view,name="home"),
    path('register/',register_view,name="register"),

    path("login/",login_user,name="login"),
    #LOGIN_REDIRECT_URL = 'dashboard'

    path("logout/",logout_user,name="logout"),
    path("profile/",profile_view ,name="profile"),
    # LOGOUT_REDIRECT_URL = 'login'  
]