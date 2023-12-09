from django import forms
from .models import Posts


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
