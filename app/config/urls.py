"""inaina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from mina.apis import MinaPostViewSet
from . import views

router = SimpleRouter()
router.register(r"mina", MinaPostViewSet)
urlpatterns_apis = [
    path("", include(router.urls)),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("mina/", include("mina.urls")),
    path("jina/", include("jina.urls")),
    path("photos/", include("photos.urls")),
    path("api/", include(urlpatterns_apis)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
