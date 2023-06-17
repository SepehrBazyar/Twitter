from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):

    age = models.PositiveIntegerField(blank=True, null=True)

    @property
    def followings_count(self) -> int:
        return self.followings.count()

    @property
    def followers_count(self) -> int:
        return self.followers.count()


    class Meta:
        verbose_name, verbose_name_plural = _("User"), _("Users")


class Relation(models.Model):

    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followings",
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers",
    )

    class Meta:
        verbose_name, verbose_name_plural = _("Relation"), _("Relations")
