from django import forms
from django.forms import inlineformset_factory
from .models import Course, Chapter, Content
 
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class':'w-full border-gray-300 rounded-lg p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder':'Course Title'}),
            'description': forms.Textarea(attrs={'class':'w-full border-gray-300 rounded-lg p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows':3, 'placeholder':'Course Description'}),
        } 
class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'description', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'w-full border-gray-300 rounded-lg p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder':'Chapter Title'}),
            'description': forms.Textarea(attrs={'class':'w-full border-gray-300 rounded-lg p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows':2, 'placeholder':'Chapter Description'}),
            'order': forms.NumberInput(attrs={'class':'w-full  border-gray-300 rounded-lg p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

ChapterFormSet = forms.inlineformset_factory(Course, Chapter, form=ChapterForm, extra=2, can_delete=True)




