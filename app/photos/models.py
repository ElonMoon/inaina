from colorfield.fields import ColorField
from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_quill.fields import QuillField

__all__ = ("PhotoPost",)


class PhotoPost(TimeStampedModel):
    title = models.CharField("제목", max_length=60)
    title_color = ColorField("제목색상", default="#333")
    subtitle = models.CharField("부제목", max_length=200, blank=True)
    subtitle_color = ColorField("부제목색상", default="#444")
    date_color = ColorField("날짜색상", default="#555")
    image_title = models.ImageField("대표이미지", blank=True)
    image_thumbnail = models.ImageField("썸네일이미지", blank=True, help_text="없을경우 대표이미지 사용")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = QuillField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "포토 포스트"
        verbose_name_plural = f"{verbose_name} 목록"
        ordering = ["-created"]
