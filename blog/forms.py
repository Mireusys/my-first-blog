"""blog Forms Configuration."""
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """blog 어플리케이션의 Form Class."""

    class Meta:
        model = Post
        fields = ('title', 'text',)
