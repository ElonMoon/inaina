from django.shortcuts import render

from notice.models import Notice


def index(request):
    context = {
        "notice_list": Notice.objects.all(),
    }
    return render(request, "common/index.html", context)


def about(request):
    return render(request, "common/about.html")
