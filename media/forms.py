from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': '2', 'placeholder': 'What\'s on your mind?'}))
    image = forms.ImageField(label='', required=False)

    class Meta:
        model = Post
        fields = ['content', 'image']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': '3', 'placeholder': 'What\'s on your mind?'}))

    class Meta:
        model = Comment
        fields = ['comment']
