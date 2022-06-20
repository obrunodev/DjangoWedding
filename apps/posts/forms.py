from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    template_name = 'form_snippet.html'
    
    
    class Meta:
        model = Post
        fields = ['text']
