from django.urls import path,include
from .views import my_view
urlpatterns =[
    path('',my_view,name="hello"),
]