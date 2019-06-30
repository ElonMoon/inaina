from django.conf.urls import url
from . import views

app_name = 'jina'
urlpatterns = [
    url(r'^post/$', views.post, name='post_default'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post, name='post'),
    url(r'^post/page/(?P<page_number>[0-9]+)/$', views.post, name='post_page_number'),
]
