from django.db import models
from core.models import BaseModel, TimeStampMixin

# Create your models here.
class Post(TimeStampMixin, BaseModel):
    text = models.TextField()
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def is_liked_by_user(self, user) -> bool:
        return self.reaction_set.filter(user=user).exists()


class Tag(models.Model):
    text = models.CharField(max_length=10)
    posts = models.ManyToManyField(Post, related_name="tags")


class Image(models.Model):
    image = models.FileField(upload_to="uploads/images/")
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=128)
    user = models.ForeignKey("accounts.User")
    post = models.ForeignKey(Post)
    reply_to = models.ForeignKey("self", blank=True, null=True)


class Reaction(BaseModel):
    user = models.ForeignKey("accounts.User")
    post = models.ForeignKey(Post)
