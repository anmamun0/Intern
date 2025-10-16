from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    ROLE_CHOICES = (
        ('agent', 'Agent'),
        ('manager', 'Manager'),
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'w-full border rounded px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full border rounded px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border rounded px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full border rounded px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full border rounded px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Confirm Password'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']

        if commit:
            user.save()
            group, _ = Group.objects.get_or_create(name=role)
            user.groups.add(group)

        return user
