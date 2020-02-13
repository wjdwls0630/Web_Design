from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    """docstring forPostForm."""
    class Meta:
        """docstring forMeta."""
        model = Post
        fields=('title','text')


class CommentForm(forms.ModelForm):
    """docstring fo CommentForm."""
    class Meta(object):
        """docstring forMeta."""
        model = Comment
        fields = ('author', 'text')
