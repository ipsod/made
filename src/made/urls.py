from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # url(r'^$', views.AdvertList.as_view(), name='home'),
    # url(r'^advert/(?P<pk>\d+)/$', views.AdvertDetail.as_view(), name='advert-detail'),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
