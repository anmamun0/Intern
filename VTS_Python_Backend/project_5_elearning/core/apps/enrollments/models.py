from django.db import models 
from apps.courses.models import Course
# Create your models here.
from .constants import STATUS_CHOICES

from django.contrib.auth import get_user_model
User = get_user_model()

class Enrollment(models.Model):
    student = models.ForeignKey(User,limit_choices_to={"role":'student'},on_delete=models.CASCADE,related_name='enrollments')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='enrollments')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='deactive')
    class Meta:
        unique_together = ['student', 'course']
        ordering = ['-created_at']
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"