from rest_framework.permissions import IsAuthenticatedOrReadOnly

from mina.models import MinaPost
from mina.serializers import MinaPostSerializer
from utils.viewsets import ModelViewSet

__all__ = ("MinaPostViewSet",)


class MinaPostViewSet(ModelViewSet):
    queryset = MinaPost.objects.all()
    serializer_class = MinaPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
