from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from .constants import TAILWIND_WIDGETS,ROLE_CHOICES

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','roll','register_id','phone_number','date_of_birth']
        widgets = {
            'username': TAILWIND_WIDGETS['CharField'](placeholder="Enter username"),
            'password': TAILWIND_WIDGETS['CharField'](placeholder="Enter Password"),
            'first_name': TAILWIND_WIDGETS['CharField'](placeholder="Enter first name"),
            'last_name': TAILWIND_WIDGETS['CharField'](placeholder="Enter last name"),
            'roll': TAILWIND_WIDGETS['CharField'](placeholder="Enter roll"),
            'register_id': TAILWIND_WIDGETS['CharField'](placeholder="Enter register ID"),
            'phone_number': TAILWIND_WIDGETS['CharField'](placeholder="Enter phone number"),
            'date_of_birth': TAILWIND_WIDGETS['DateField'](),
        }