from django.contrib import admin

# Register your models here.
from .models import Course,Chapter,Content

# -----------------------------
# Inline for Chapter (inside Course)
# -----------------------------
class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1
 
# -----------------------------
# Inine for Content (inside Chapter)
# -----------------------------
class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


# -----------------------------
# Course Admin
# -----------------------------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['get_mentor_username','title', 'description']
    list_filter = ['mentor__role']
    inlines = [ChapterInline]

    def get_mentor_username(self, obj):
        return obj.mentor.username
    get_mentor_username.short_description ="Mentor"
 
# -----------------------------
# Chapter Admin
# -----------------------------
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['get_course_title','title','order']
    list_filter = ['course']
    inlines = [ContentInline]
    # search_fields = ['course__title']

    def get_course_title(self,obj):
        return obj.course.title
    get_course_title.short_description = "Course Title"

# -----------------------------
# Content Admin
# -----------------------------
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['chapter','title','video_url','order']
    def get_chapter_title(self,obj):
        return obj.chapter.title
    get_chapter_title.short_description = "Chapter Title"