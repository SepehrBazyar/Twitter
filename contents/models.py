from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core.models import (
    BaseModel,
    SoftDeleteModel,
    TimeStampMixin,
)

# Create your models here.
class Tag(BaseModel):
    text = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.text


class Post(TimeStampMixin, SoftDeleteModel):

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    class Statuses(models.TextChoices):
        DRAFT = "D", _("Draft")
        PUBLISHED = "P", _("Published")

    text = models.TextField(verbose_name=_("Title"), help_text=_("Text to display"))
    title = models.CharField(_("Title"), max_length=124)
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    status = models.CharField(
        max_length=1,
        choices=Statuses.choices,
        default=Statuses.PUBLISHED,
    )
    tags = models.ManyToManyField(Tag, related_name="posts")

    def get_url(self):
        return reverse('contents:detail', args=(self.id,))

    def __str__(self) -> str:
        return self.text


class Image(BaseModel):
    photo = models.FileField(upload_to="posts/images/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")


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
