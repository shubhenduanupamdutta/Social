from django import forms
from .models import Posts


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("title", "image", "caption")
