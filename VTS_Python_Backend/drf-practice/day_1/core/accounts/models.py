from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
 

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)  
    designation = models.CharField(max_length=150, blank=True) 
    
    def __str__(self):
        return self.username
    

class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()


class Links(models.Model):
    platform = models.CharField(max_length=150)
    url = models.URLField()
    students = models.ManyToManyField(Student,related_name='links',blank=True)

