from django import forms
from django.contrib.auth import get_user_model,authenticate
User = get_user_model()
from .constants import Custom_Widget,ROLE_CHOICES

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','roll','register_id','email','phone_number','date_of_birth','profile_image'] 
        widgets = Custom_Widget

class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=150)
    password = forms.CharField() 

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username_or_email')
        password = cleaned_data.get('password')
        user = authenticate(email=username_or_email, password=password)
        if not user:
            try :
                user_obj = User.objects.get(username=username_or_email)
                user = authenticate(email=user_obj.email, password=password)
            except User.DoesNotExist:
                user = None    
        if not user:
            raise forms.ValidationError("Username / Email not validate!")
            
        self.user = user
        return cleaned_data


    
     