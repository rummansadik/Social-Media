from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': '3', 'placeholder': 'What\'s on your mind?'}))

    class Meta:
        model = Post
        fields = ['content']
