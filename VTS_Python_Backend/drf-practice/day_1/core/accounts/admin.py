from django.contrib import admin

# Register your models here.
from .models import Student,Links

admin.site.register(Student)
admin.site.register(Links)