from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mobile/$', views.index1, name="index1"),
    url(r'^toys/$', views.index2, name="index2"),
    url(r'mobile/(?P<id>[0-9]+)/$', views.detail, name="detail"),
    url(r'toys/(?P<id>[0-9]+)/$', views.more, name="more"),
   # url(r'tv/(?P<id>[0-9]+)/, m.')
]