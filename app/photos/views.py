from django.shortcuts import render, get_object_or_404

from photos.models import PhotoPost

__all__ = (
    "thumbnails",
    "photo_post",
)


def thumbnails(request):
    posts = PhotoPost.objects.defer("content")
    context = {
        "posts": posts,
    }
    return render(request, "photo/thumbnails.html", context)


def photo_post(request, pk):
    post = get_object_or_404(PhotoPost, pk=pk)
    context = {
        "post": post,
    }
    return render(request, "photo/post.html", context)
