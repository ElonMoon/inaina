from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet as DefaultGenericViewSet

__all__ = (
    "ViewSetMixin",
    "ListModelViewSet",
    "CreateModelViewSet",
    "RetrieveModelViewSet",
    "UpdateModelViewSet",
    "DestroyModelViewSet",
    "RetrieveUpdateModelViewSet",
    "RetrieveUpdateDestroyModelViewSet",
    "ReadOnlyModelViewSet",
    "ModelViewSet",
)


class GetSerializerClassMixin:
    serializer_classes = {}

    def get_serializer_class(self):
        try:
            action = getattr(self, "action")
            method = getattr(getattr(self, "request"), "method")

            if action:
                if action == "partial_update":
                    action = "update"
                return self.serializer_classes[action]
            if method:
                return self.serializer_classes[self.request.method]
        except (KeyError, AttributeError):
            pass
        return super().get_serializer_class()


class ViewSetMixin(GetSerializerClassMixin):
    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs and isinstance(kwargs["data"], list):
            kwargs.setdefault("many", True)
        return super().get_serializer(*args, **kwargs)


class DestroyModelMixin(mixins.DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_destroy(instance, serializer)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AssertionError:
            return super().destroy(request, *args, **kwargs)

    def perform_destroy(self, instance, serializer=None):
        if serializer:
            serializer.save()
        else:
            return super().perform_destroy(instance)


class ListModelViewSet(ViewSetMixin, mixins.ListModelMixin, DefaultGenericViewSet):
    pass


class CreateModelViewSet(ViewSetMixin, mixins.CreateModelMixin, DefaultGenericViewSet):
    pass


class RetrieveModelViewSet(ViewSetMixin, mixins.RetrieveModelMixin, DefaultGenericViewSet):
    pass


class UpdateModelViewSet(ViewSetMixin, mixins.UpdateModelMixin, DefaultGenericViewSet):
    pass


class DestroyModelViewSet(ViewSetMixin, mixins.DestroyModelMixin, DefaultGenericViewSet):
    pass


class RetrieveUpdateModelViewSet(
    ViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    DefaultGenericViewSet,
):
    pass


class RetrieveUpdateDestroyModelViewSet(
    ViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    DestroyModelMixin,
    DefaultGenericViewSet,
):
    pass


class ReadOnlyModelViewSet(
    ViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    DefaultGenericViewSet,
):
    pass


class ModelViewSet(
    ViewSetMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    DestroyModelMixin,
    mixins.ListModelMixin,
    DefaultGenericViewSet,
):
    pass
