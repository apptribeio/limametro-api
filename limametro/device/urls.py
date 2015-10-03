from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^register$', 'limametro.device.views.register', name='device_register'),
)
