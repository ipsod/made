from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # --Administration--------------------------------------

    # Thing Categories
    url(r'^category/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category_detail, name='category_detail'),
    url(r'^category/create/$', views.CategoryCreate.as_view(), name='category_create'),
    url(r'^category/(?P<pk>[0-9]+)/edit/$', views.CategoryUpdate.as_view(), name='category_edit'),
    url(r'^category/(?P<pk>[0-9]+)/delete/$', views.CategoryDelete.as_view(), name='category_delete'),

    # Things
    url(r'^(?P<thing_sku>[0-9]+)/$', views.thing_detail, name='thing_detail'),
    url(r'^(?P<thing_sku>[0-9]+)/create/in_category/(?P<category_id>[0-9]+)$', views.create_thing, name='thing_create'),
    url(r'^(?P<thing_sku>[0-9]+)/edit/$', views.edit_thing, name='thing_edit'),
    url(r'^(?P<thing_sku>[0-9]+)/delete/$', views.ThingDelete.as_view(), name='thing_delete'),

    # Thing Attributes
    url(r'^attribute/$', views.AttributeList.as_view(), name='attribute_list'),
    url(r'^attribute/(?P<pk>[0-9]+)/$', views.AttributeDetail.as_view(), name='attribute_detail'),
    url(r'^attribute/create/$', views.AttributeCreate.as_view(), name='attribute_create'),
    url(r'^attribute/(?P<pk>[0-9]+)/edit/$', views.AttributeUpdate.as_view(), name='attribute_edit'),
    url(r'^attribute/(?P<pk>[0-9]+)/delete/$', views.AttributeDelete.as_view(), name='attribute_delete'),
]
