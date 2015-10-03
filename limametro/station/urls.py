from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all$', 'limametro.station.views.all', name='station_all'),
    url(r'^(?P<code>[a-fA-F\d]{32})$', 'limametro.station.views.details', name='station_details'),
    url(r'^(?P<code>[a-fA-F\d]{32})/services$', 'limametro.station.views.services', name='station_services'),
)