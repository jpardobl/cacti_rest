from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^host/(\d+)/data_sources', 'cacti_rest.resource_host_datasource.entrance', name='resource_host_datasource'),
    url(r'^host', 'cacti_rest.resource_host.entrance', name='resource_host'),    
    url(r'^data_source/(\d+)', 'cacti_rest.resource_datasource.entrance', name='resource_datasource'),
)
