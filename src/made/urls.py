from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # url(r'^$', views.AdvertList.as_view(), name='home'),
    # url(r'^advert/(?P<pk>\d+)/$', views.AdvertDetail.as_view(), name='advert-detail'),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/', include('catalog.urls')),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Required in Development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
