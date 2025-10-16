 
from django.contrib import admin
from django.urls import path
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
]
