 
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
