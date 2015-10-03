from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^devices/', include('limametro.device.urls')),
    url(r'^stations/', include('limametro.station.urls')),
    url(r'^services/', include('limametro.service.urls')),
)
