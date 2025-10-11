from django.contrib import admin

# Register your models here.
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display  = ['get_student','get_course','status']

    def get_student(self,obj):
        return obj.student.username
    get_student.short_description = "Studnet"

    def get_course(self,obj):
        return f"{obj.course.mentor.username} - {obj.course.title}"
    get_course.short_description = "Mentor"