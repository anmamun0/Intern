from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),  
    path("user/",include("accounts.urls")) , 

    path("",include("servants.urls")) , 
    
]






# Youtube: @anCoder
# Github: mhttps://github.com/anmamun0
# portfolio: https://anmamun0.vercel.app/

# Generic Views: https://docs.djangoproject.com/en/5.2/ref/class-based-views/
# Blogs: https://www.django-rest-framework.org/api-guide/generic-views/