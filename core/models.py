from django.db import models
from uuid import uuid4

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class SoftDeleteModel(BaseModel):
    is_deleted = models.BooleanField(default=False, db_index=True)

    def delete(self):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True


class TimeStampMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
