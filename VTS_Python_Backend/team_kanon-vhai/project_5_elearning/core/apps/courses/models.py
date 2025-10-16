from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

# -----------------------------
# Course Model
# -----------------------------
class Course(models.Model):
    mentor = models.ForeignKey(User,limit_choices_to={'role':'mentor'},on_delete=models.CASCADE,related_name='courses') 
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    created_at =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['-created_at']
 
    def __str__(self):
        return self.title 
        
    def get_student(self):
        return self.enrollments.count() 
    
# -----------------------------
# Chapter Model
# -----------------------------

class Chapter(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='chapters')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    order = models.PositiveIntegerField(help_text='Sequence Number Sequence Chapter')
    created_at =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural= "Chapters"
        ordering  = ['order']

    def __str__(self):
        return f"{self.title} ({self.course.title})"

# -----------------------------
# Content Model
# -----------------------------
class Content(models.Model):
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE,related_name='contents')
    title = models.CharField(max_length=255) 
    video_url = models.URLField(max_length=255)
    order = models.PositiveIntegerField(help_text='Sequence Number Sequence Content')
    created_at =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.chapter.title})"