from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class MyUser(models.Model):
    username = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
        verbose_name=_("Username"),
        help_text=_("Username to login and show in the profile"),
        blank=False,
        null=False,
    )
    password = models.CharField(
        max_length=128,
        verbose_name=_("Password"),
        help_text=_("Password to login and authenticate"),
        blank=False,
        null=False,
    )
    photo = models.FileField(
        upload_to="uploads/photos/",
    )


class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followings")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)
