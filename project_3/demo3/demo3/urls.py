from django.contrib import admin
from django.urls import path,include 


apps_urlpatterns =[
    path("user/",include("apps.accounts.urls")) , 
    path("",include("apps.employes.urls")) , 
]


urlpatterns = (
    [
        path('admin/', admin.site.urls),      
    ]
    + apps_urlpatterns 
)

 



# Youtube: @anCoder
# Github: mhttps://github.com/anmamun0
# portfolio: https://anmamun0.vercel.app/

# Generic Views: https://docs.djangoproject.com/en/5.2/ref/class-based-views/
# Blogs: https://www.django-rest-framework.org/api-guide/generic-views/