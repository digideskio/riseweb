from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<id>\d)/$', views.article, name='article'),
    url(r'^score/(?P<series_id>[0-9]+)/(?P<match_id>[0-9]+)/$', views.score, name='score'),
]