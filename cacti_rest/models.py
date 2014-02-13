# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
import simplejson


class Host(models.Model):
    id = models.IntegerField(primary_key=True)
    host_template_id = models.IntegerField()
    description = models.CharField(max_length=150L)
    hostname = models.CharField(max_length=250L, blank=True)
    notes = models.TextField(blank=True)
    snmp_community = models.CharField(max_length=100L, blank=True)
    snmp_version = models.IntegerField()
    snmp_username = models.CharField(max_length=50L, blank=True)
    snmp_password = models.CharField(max_length=50L, blank=True)
    snmp_auth_protocol = models.CharField(max_length=5L, blank=True)
    snmp_priv_passphrase = models.CharField(max_length=200L, blank=True)
    snmp_priv_protocol = models.CharField(max_length=6L, blank=True)
    snmp_context = models.CharField(max_length=64L, blank=True)
    snmp_port = models.IntegerField()
    snmp_timeout = models.IntegerField()
    availability_method = models.IntegerField()
    ping_method = models.IntegerField(null=True, blank=True)
    ping_port = models.IntegerField(null=True, blank=True)
    ping_timeout = models.IntegerField(null=True, blank=True)
    ping_retries = models.IntegerField(null=True, blank=True)
    max_oids = models.IntegerField(null=True, blank=True)
    device_threads = models.IntegerField()
    disabled = models.CharField(max_length=2L, blank=True)
    thold_send_email = models.IntegerField()
    thold_host_email = models.IntegerField()
    monitor = models.CharField(max_length=3L)
    monitor_text = models.TextField()
    status = models.IntegerField()
    status_event_count = models.IntegerField()
    status_fail_date = models.DateTimeField()
    status_rec_date = models.DateTimeField()
    status_last_error = models.CharField(max_length=255L, blank=True)
    min_time = models.DecimalField(null=True, max_digits=12, decimal_places=5, blank=True)
    max_time = models.DecimalField(null=True, max_digits=12, decimal_places=5, blank=True)
    cur_time = models.DecimalField(null=True, max_digits=12, decimal_places=5, blank=True)
    avg_time = models.DecimalField(null=True, max_digits=12, decimal_places=5, blank=True)
    total_polls = models.IntegerField(null=True, blank=True)
    failed_polls = models.IntegerField(null=True, blank=True)
    availability = models.DecimalField(max_digits=10, decimal_places=5)
    class Meta:
        db_table = 'host'
        
    def to_json(self):
        return simplejson.dumps({
            "resource_type": "host",
            "hostname": self.hostname, 
            "id": self.id, 
            "description": self.description,
            "datasources": reverse('resource_host_datasource', args=[self.id, ])})
        

class DataTemplateData(models.Model):
    id = models.IntegerField(primary_key=True)
    local_data_template_data_id = models.IntegerField()
    local_data_id = models.ForeignKey("DataLocal", db_column="local_data_id", related_name="template")
    data_template_id = models.ForeignKey("DataTemplate", db_column="data_template_id")
    data_input_id = models.IntegerField()
    t_name = models.CharField(max_length=2L, blank=True)
    name = models.CharField(max_length=250L)
    name_cache = models.CharField(max_length=255L)
    data_source_path = models.CharField(max_length=255L, blank=True)
    t_active = models.CharField(max_length=2L, blank=True)
    active = models.CharField(max_length=2L, blank=True)
    t_rrd_step = models.CharField(max_length=2L, blank=True)
    rrd_step = models.IntegerField()
    t_rra_id = models.CharField(max_length=2L, blank=True)
    class Meta:
        db_table = 'data_template_data'
        
    def __unicode__(self):
        return u"%s" % self.name

class DataTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    name = models.CharField(max_length=150L)
    class Meta:
        db_table = 'data_template'
        
class DataLocal(models.Model):
    id = models.IntegerField(primary_key=True)
    data_template_id = models.ForeignKey(DataTemplateData, db_column="data_template_id")
    host_id = models.ForeignKey(Host,db_column="host_id")
    snmp_query_id = models.IntegerField()
    snmp_index = models.CharField(max_length=255L)
    class Meta:
        db_table = 'data_local'
        
    def to_json(self):
        return simplejson.dumps({
                "resource_type": "datasource",
                "id": self.id, 
                "host_id": self.host_id.description, 
                "template": u"%s" % self.template.get().data_template_id.name,
                "data": reverse('resource_datasource', args=[self.id, ]),
                })
        
    def get_rra_path(self):
        return self.data_template_id.data_source_path

class Settings(models.Model):
    name = models.CharField(max_length=50L, primary_key=True)
    value = models.CharField(max_length=1024L)
    class Meta:
        db_table = 'settings'
