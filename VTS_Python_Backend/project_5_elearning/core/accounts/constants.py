ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('mentor', 'Mentor'),
    ('student', 'Student'),
)


# widgets.py
from django import forms

# Base Tailwind classes
TAILWIND_INPUT_CLASS = "block w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"

# Dictionary mapping Django field types to Tailwind widgets
# Tailwind Widgets dictionary
TAILWIND_WIDGETS = {
    'CharField': lambda **kwargs: forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASS, **kwargs}),
    'EmailField': lambda **kwargs: forms.EmailInput(attrs={'class': TAILWIND_INPUT_CLASS, **kwargs}),
    'PasswordField': lambda **kwargs: forms.PasswordInput(attrs={'class': TAILWIND_INPUT_CLASS, **kwargs}),
    'DateField': lambda **kwargs: forms.DateInput(attrs={'type': 'date', 'class': TAILWIND_INPUT_CLASS, **kwargs}),
}
