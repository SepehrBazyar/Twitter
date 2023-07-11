from django import forms
from .models import Post


class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        # fields = ("title", "text")
        exclude = ["user", "is_deleted"]
