from django import forms
from .models import Comment, Posts


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("title", "image", "caption")

    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full focus:outline-none'
            })


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
