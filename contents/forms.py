from django import forms
from .models import Post, Comment


class PostUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        # fields = ("title", "text")
        exclude = ["user", "is_deleted"]


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("text",)
