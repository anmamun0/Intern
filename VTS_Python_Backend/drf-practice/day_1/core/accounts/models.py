from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
 

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)  
    designation = models.CharField(max_length=150, blank=True) 
    
    def __str__(self):
        return self.username