from django.urls import path

from . import views

app_name = "photos"
urlpatterns = [
    path("", views.thumbnails, name="thumbnails"),
    path("posts/<int:pk>/", views.photo_post, name="posts"),
]
