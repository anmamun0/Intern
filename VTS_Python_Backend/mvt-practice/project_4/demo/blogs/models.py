from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_blogs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)