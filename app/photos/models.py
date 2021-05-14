from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_quill.fields import QuillField

__all__ = ("PhotoPost",)


class PhotoPost(TimeStampedModel):
    title = models.CharField(max_length=60)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = QuillField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "포토 포스트"
        verbose_name_plural = f"{verbose_name} 목록"
        ordering = ["-created"]
