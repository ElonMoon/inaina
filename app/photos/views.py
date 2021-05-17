from django.shortcuts import render

from photos.models import PhotoPost


def thumbnails(request):
    posts = PhotoPost.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "photo/thumbnails.html", context)
