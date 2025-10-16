from django.shortcuts import render ,redirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, View
from django.contrib.auth.models import User 
from django.contrib.auth import login
from .forms import RegisterForm 
from django.urls import reverse_lazy  

class RegisterView(CreateView):
    model = User 
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        
        user = form.save(commit=False)
        user.is_active = False  
        user.save()

        res = super().form_valid(form)
        # login(self.request,self.object)
        return res   
    
from django.contrib import messages  
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator 
     
class VerifyEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except:
            user = None 
        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Email verified! You can now login.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid or expired verification link.')
            return redirect('register')
 
def email_verification_sent(request):
    return render(request, 'email_verification_sent.html')

 