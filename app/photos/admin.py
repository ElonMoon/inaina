from django.contrib import admin

from photos.models import PhotoPost


@admin.register(PhotoPost)
class PhotoPostAdmin(admin.ModelAdmin):
    pass
