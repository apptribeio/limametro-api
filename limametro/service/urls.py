from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all$', 'limametro.service.views.all', name='services_all'),
)