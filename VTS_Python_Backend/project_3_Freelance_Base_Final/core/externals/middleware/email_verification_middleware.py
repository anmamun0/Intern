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
                    request.session['pending_user_id'] = user.id  # store temporarily
                    return redirect(reverse('email_verification_pending'))

        response = self.get_response(request)
        return response
  