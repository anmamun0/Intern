ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('mentor', 'Mentor'),
    ('student', 'Student'),
)


# widgets.py
from django import forms 
TAILWIND_INPUT_CLASS = "block w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
 
TAILWIND_WIDGETS = {
    'CharField': lambda **kwargs: forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASS, **kwargs}),
    'EmailField': lambda **kwargs: forms.EmailInput(attrs={'class': TAILWIND_INPUT_CLASS, **kwargs}),
    'PasswordField': lambda **kwargs: forms.PasswordInput(attrs={'class': TAILWIND_INPUT_CLASS, **kwargs}),
    'DateField': lambda **kwargs: forms.DateInput(attrs={'type': 'date', 'class': TAILWIND_INPUT_CLASS, **kwargs}),
}
 
Custom_Widget = {
    'username': TAILWIND_WIDGETS['CharField'](placeholder="Enter username"),
    'password': TAILWIND_WIDGETS['CharField'](placeholder="Enter Password"),
    'first_name': TAILWIND_WIDGETS['CharField'](placeholder="Enter first name"),
    'last_name': TAILWIND_WIDGETS['CharField'](placeholder="Enter last name"),
    'email': TAILWIND_WIDGETS['EmailField'](placeholder="Enter Email"),
    'roll': TAILWIND_WIDGETS['CharField'](placeholder="Enter roll"),
    'register_id': TAILWIND_WIDGETS['CharField'](placeholder="Enter register ID"),
    'phone_number': TAILWIND_WIDGETS['CharField'](placeholder="Enter phone number"),
    'date_of_birth': TAILWIND_WIDGETS['DateField'](),
}