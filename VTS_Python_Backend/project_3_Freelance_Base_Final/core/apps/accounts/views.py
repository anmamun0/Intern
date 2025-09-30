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
    template_name = "accounts/register.html"
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
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

# ----------------------------------------------- 
def email_verification_pending(request):
    user_id = request.session.get('pending_user_id')
    if not user_id:
        return redirect('login')
    user = User.objects.get(id=user_id)
    return render(request, 'accounts/email_verification_pending.html', {'user': user})
 
def send_verification_email(request):
    user_id = request.session.get('pending_user_id')
    if not user_id:
        return redirect('login')
    user = User.objects.get(id=user_id)

    current_site = get_current_site(request)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    verification_link = f"http://{current_site.domain}/user/verify-email/{uid}/{token}/"

    message = render_to_string('accounts/email_verification.html', {
        'user': user,
        'verification_link': verification_link,
    })
    email = EmailMultiAlternatives(
        subject="Verify your email",
        body="",
        from_email="VTS <noreply@example.com>",
        to=[user.email],
    )
    email.attach_alternative(message, "text/html")
    email.send()

    return render(request, "accounts/email_verification_sent.html")


# -----------------------------------------------


 

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
    return render(request, 'accounts/email_verification_sent.html')

 