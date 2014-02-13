from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^v1/host/(\d+)/data_sources', 'cacti_rest.resource_host_datasource.entrance', name='resource_host_datasource'),
    url(r'^v1/host/(\d+)', 'cacti_rest.resource_host.entrance', name='resource_host'),
    url(r'^v1/hosts', 'cacti_rest.resource_hosts.entrance', name='resource_hosts'),    
    
    url(r'^v1/data_source/(\d+)', 'cacti_rest.resource_datasource.entrance', name='resource_datasource'),
)
