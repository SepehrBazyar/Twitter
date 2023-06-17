from django.db import models
from core.models import (
    BaseModel,
    SoftDeleteModel,
    TimeStampMixin,
)

# Create your models here.
class Post(TimeStampMixin, SoftDeleteModel):
    text = models.TextField()
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )


class Tag(BaseModel):
    text = models.CharField(max_length=10)
    posts = models.ManyToManyField(Post, related_name="tags")


class Comment(BaseModel):
    text = models.CharField(max_length=128)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )


class Reaction(BaseModel):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
