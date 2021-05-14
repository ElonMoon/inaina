from django.db import models

from config.models import BaseModel


class Notice(BaseModel):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "%s 목록" % verbose_name
        ordering = ("-created_date",)

    def __str__(self):
        return self.title
