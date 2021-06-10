from rest_framework import serializers

from mina.models import MinaPost

__all__ = ("MinaPostSerializer",)


class MinaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinaPost
        fields = (
            "id",
            "title",
            "image",
            "content",
            "description",
        )
