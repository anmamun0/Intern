from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .constants import STATUS_CHOICES

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


 

class LeaveRequest(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.agent.username} - {self.start_date} to {self.end_date}"
    
    class Meta:
        ordering = ['-created_at']

    def clean(self): 
        if not self.agent: 
            return

        if self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after end date.")
 
        overlapping_request = LeaveRequest.objects.filter(
            agent=self.agent,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        ).exclude(id=self.id).first()
        
        if overlapping_request:
            raise ValidationError(
                f"You already have a leave request from {overlapping_request.start_date} to {overlapping_request.end_date}."
            )

         
        approved_request = LeaveRequest.objects.filter(
            agent=self.agent,
            status='approved',
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        ).exclude(id=self.id).first()

        if approved_request:
            raise ValidationError(
                f"You already have an approved leave from {approved_request.start_date} to {approved_request.end_date}. You cannot apply again in this period."
            )

    def save(self, *args, **kwargs):
        self.full_clean()   
        super().save(*args, **kwargs)
