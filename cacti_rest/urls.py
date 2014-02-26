from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^v1/host/(\d+)/data_sources', 'cacti_rest.resource_host_datasource.entrance', name='resource_host_datasource'),
    url(r'^v1/host/(\d+)', 'cacti_rest.resource_host.entrance', name='resource_host'),
    url(r'^v1/hosts', 'cacti_rest.resource_hosts.entrance', name='resource_hosts'),    
    url(r'^v1/data_source/(\d+)', 'cacti_rest.resource_datasource.entrance', name='resource_datasource'),
    
    url(r'^v1/data_input_method/(?P<pk>[0-9]+)/$', DataInputDetail.as_view(), name='datainput-detail'),
    url(r'^v1/data_input_methods/?$', DataInputList.as_view(), name='datainput-list'),
    
    url(r'^v1/data_input_field/(?P<pk>[0-9]+)/$', DataInputFieldsDetail.as_view(), name='datainputfields-detail'),
    url(r'^v1/data_input_fields/?$', DataInputFieldsList.as_view(), name='datainputfields-list'),
    
    url(r'^v1/host_template/(?P<pk>[0-9]+)/$', HostTemplateDetail.as_view(), name='hosttemplate-detail'),
    url(r'^v1/host_templates/?$', HostTemplateList.as_view(), name='hosttemplate-list'),
    
    url(r'^v2/host/(?P<pk>[0-9]+)/$', HostDetail.as_view(), name='host-detail'),
    url(r'^v2/hosts/?$', HostList.as_view(), name='host-list'),
    
   
)
