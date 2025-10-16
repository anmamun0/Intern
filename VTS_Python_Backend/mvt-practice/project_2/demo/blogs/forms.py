from django import forms
from .models import Blog ,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter blog title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 h-40 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Write your blog content...'
            }),
        }

 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                    'rows': 3,
                    'placeholder': 'Write your comment here...',
                }
            ),
        }
        labels = {
            'content': '',  # hide label
        }