from django.urls import path, include
from .views import RegisterView 
from django.contrib.auth.views import LoginView,LogoutView
from .views import VerifyEmailView,email_verification_sent,email_verification_pending,send_verification_email


urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path("login/",LoginView.as_view(template_name="accounts/login.html"),name="login"),
    #LOGIN_REDIRECT_URL = 'dashboard'

    path("logout/",LogoutView.as_view(),name="logout"),
    # LOGOUT_REDIRECT_URL = 'login'  
    

    path('verify-pending/', email_verification_pending, name='email_verification_pending'),
    path('send-verification/', send_verification_email, name='send_verification_email'), 

    #  -------------- verification back
    path('verify-email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('email-verification-sent/', email_verification_sent, name='email_verification_sent'),
]

  
 

 
   
 