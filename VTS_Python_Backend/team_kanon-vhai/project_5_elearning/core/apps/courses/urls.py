from django.urls import path,include
from .views import course_view,course_detail_view 
from . import views
urlpatterns = [
    path('courses/',course_view,name="courses"),
    path('course_details/<int:course_id>/',course_detail_view,name='course_details'),
    # path('courses/create/',course_create,name='course_create'),
    path('courses/create/', views.course_create, name='course_create'), 

      # Course URLs
    # path('courses/create/',  create_course, name='create_course'),
    # path('<int:course_id>/chapter/create/',  create_chapter, name='create_chapter'),
    # path('chapter/<int:chapter_id>/content/create/', create_content, name='create_content'),
    
    # Add these if you need them  
    # path('chapter/<int:chapter_id>/',  chapter_detail, name='chapter_detail'),

 
    # path('courses/add/', views.course_create, name='course_create'),
]