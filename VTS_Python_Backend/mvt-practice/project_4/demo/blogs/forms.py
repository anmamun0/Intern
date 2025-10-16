from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
    def __init__(self, *args, **kwargs):
        print("initial")
        super().__init__(*args, **kwargs)  # প্রথমে parent init কল করা নিরাপদ

        # এখন model, fields, instance, data ইত্যাদি print করা যাক
        print("Model name:", self._meta.model.__name__)  # 'Blog'
        print("Fields:", list(self.fields.keys()))        # ['title', 'content', 'image']
        print("Instance:", self.instance)                 # যদি edit form হয়, তাহলে model instance দেখাবে
        print("Initial data:", self.initial)              # যদি initial data থাকে, দেখাবে
        print("Data (POST):", self.data)                  # যদি POST data আসে, দেখাবে

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        # Short validations
        if title and len(title) < 5:
            self.add_error('title', "Title must be at least 5 characters.")
        if content and len(content) < 10:
            self.add_error('content', "Content must be at least 10 characters.")

        return cleaned_data