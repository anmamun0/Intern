from django.shortcuts import render, get_object_or_404,redirect
from .models import Course, Chapter, Content
 
from django.contrib import messages

def course_view(request): 
    courses = Course.objects.all().prefetch_related('chapters', 'enrollments')
 
    return render(request, template_name='courses/courses.html', context={ "courses": courses})


def course_detail_view(request, course_id): 
    course = get_object_or_404(Course.objects.prefetch_related('chapters__contents'), id=course_id)
     
    chapters = course.chapters.all().order_by('order')
    
    context = {
        "course": course,
        "chapters": chapters,
    }
    return render(request, template_name='courses/course_detail.html', context=context)

# -----------------------------
# Course Views
# -----------------------------
 # views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CourseForm, ChapterFormSet
from .models import Course, Chapter, Content

@login_required
def course_create(request):
    if request.user.role != 'mentor':
        messages.error(request, "Only mentors can create courses.")
        return redirect('courses')

    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        chapter_formset = ChapterFormSet(request.POST, prefix='chapters')

        if course_form.is_valid() and chapter_formset.is_valid():
            course = course_form.save(commit=False)
            course.mentor = request.user
            course.save()

            chapters = chapter_formset.save(commit=False)
            for idx, chapter in enumerate(chapters):
                chapter.course = course
                chapter.save()

                # Save contents manually
                content_titles = request.POST.getlist(f'chapter-{idx}-content-title')
                content_videos = request.POST.getlist(f'chapter-{idx}-content-video')
                content_orders = request.POST.getlist(f'chapter-{idx}-content-order')
                for t, v, o in zip(content_titles, content_videos, content_orders):
                    if t.strip():
                        Content.objects.create(chapter=chapter, title=t, video_url=v, order=int(o))

            messages.success(request, "created successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please fix errors below.")
    else:
        course_form = CourseForm()
        chapter_formset = ChapterFormSet(prefix='chapters')

    return render(request, 'courses/course_create.html', {
        'course_form': course_form,
        'chapter_formset': chapter_formset,
    })
