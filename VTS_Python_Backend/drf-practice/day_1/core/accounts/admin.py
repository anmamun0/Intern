from django.contrib import admin

# Register your models here.
from .models import Student,Links,CustomUser

admin.site.register(Student)
admin.site.register(Links)
admin.site.register(CustomUser)