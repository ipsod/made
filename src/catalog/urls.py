from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<thing_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^category/$', views.category, name='detail'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='detail'),
]
