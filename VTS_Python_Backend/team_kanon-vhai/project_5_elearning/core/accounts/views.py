from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,get_user_model,logout
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from apps.enrollments.models import Enrollment

# Create your views here.
User = get_user_model()

def home_view(request):
    return render(request,'home.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('profile') 
    else:
        form = RegisterForm() 
    return render(request, "accounts/register.html", {'form': form})
  
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():  
            login(request,form.user)
            return redirect('profile')
    else:
        form = LoginForm() 
    return render(request, "accounts/login.html", {"form": form})

def logout_user(request):
    if request.user :
        logout(request)
        return redirect('login')
    return redirect('profile')

@login_required
def profile_view(request):
    user = request.user
    enrolled_courses = []
    uploaded_courses = []
    enrolled = []

    if user.role == 'student':
        enrolled_courses = user.enrollments.filter(status='active')  
    elif user.role == 'mentor':
        uploaded_courses = user.courses.all()   
        enrolled = Enrollment.objects.filter(course__mentor=user)
        

    return render(request, 'accounts/profile.html', {
        'enrolled_courses': enrolled_courses,
        'uploaded_courses': uploaded_courses,
        'enrolled': enrolled,
    })