from django.urls import path

from . import views

app_name = "mina"
urlpatterns = [
    path("post/", views.post, name="post_default"),
    path("post/<int:pk>/", views.post, name="post"),
    path("post/page/<int:page_number>/", views.post, name="post_page_number"),
]
