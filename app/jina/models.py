from django.conf import settings
from django.contrib.auth import get_user_model

from config.models import *

User = get_user_model()


class JinaPost(BaseModel):
    title = models.CharField(max_length=60)
    user = models.ForeignKey(
        User,
        verbose_name="유저",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to="jina/", blank=True)
    content = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "지나 포스트"
        verbose_name_plural = "%s 목록" % verbose_name
        ordering = ("-created_date",)

    def __str__(self):
        return self.title
