 
from django.contrib import admin
from django.urls import path,include
from .views import BlogDetailView,BlogListView,BlogCreateView,BlogDeleteView
urlpatterns = [
    path('details/<int:pk>',BlogDetailView.as_view(),name="blog_detail"),  
    path("blogs/", BlogListView.as_view(), name="blogs_list"),
     path('add/', BlogCreateView.as_view(), name='write_blog'),
     path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]


