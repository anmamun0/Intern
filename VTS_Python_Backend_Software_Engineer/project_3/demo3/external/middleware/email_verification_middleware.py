from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

class EmailVerificationMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request): 
        if request.path == reverse('login') and request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            if username and password:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = None

                if user and not user.is_active: 
                        self.send_verification_email(request, user) 
                        return redirect(reverse('email_verification_sent'))

        response = self.get_response(request)
        return response

    def send_verification_email(self, request, user):
        current_site = get_current_site(request)
        subject = 'Verify your email'
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        verification_link = f"http://{current_site.domain}/user/verify-email/{uid}/{token}/"

        message = render_to_string('email_verification.html', {
            'user': user,
            'verification_link': verification_link,
        })
        email = EmailMultiAlternatives(
            subject="Login successful",
            body='',
            from_email= 'VTS <noreply@example.com>', 
            to = [user.email],
        )
        email.attach_alternative(message, "text/html")
        email.send()
 