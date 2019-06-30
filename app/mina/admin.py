from django.contrib import admin
from .models import MinaPost


class MinaPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', )


admin.site.register(MinaPost, MinaPostAdmin)
