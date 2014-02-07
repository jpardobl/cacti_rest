# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Cdef(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'cdef'

class CdefItems(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    cdef_id = models.IntegerField()
    sequence = models.IntegerField()
    type = models.IntegerField()
    value = models.CharField(max_length=150L)
    class Meta:
        db_table = 'cdef_items'

class Colors(models.Model):
    id = models.IntegerField(primary_key=True)
    hex = models.CharField(max_length=6L)
    class Meta:
        db_table = 'colors'

class DataInput(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    name = models.CharField(max_length=200L)
    input_string = models.CharField(max_length=255L, blank=True)
    type_id = models.IntegerField()
    class Meta:
        db_table = 'data_input'

class DataInputData(models.Model):
    data_input_field_id = models.IntegerField()
    data_template_data_id = models.IntegerField()
    t_value = models.CharField(max_length=2L, blank=True)
    value = models.TextField(blank=True)
    class Meta:
        db_table = 'data_input_data'

class DataInputFields(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    data_input_id = models.IntegerField()
    name = models.CharField(max_length=200L)
    data_name = models.CharField(max_length=50L)
    input_output = models.CharField(max_length=3L)
    update_rra = models.CharField(max_length=2L, blank=True)
    sequence = models.IntegerField()
    type_code = models.CharField(max_length=40L, blank=True)
    regexp_match = models.CharField(max_length=200L, blank=True)
    allow_nulls = models.CharField(max_length=2L, blank=True)
    class Meta:
        db_table = 'data_input_fields'

class DataLocal(models.Model):
    id = models.IntegerField(primary_key=True)
    data_template_id = models.IntegerField()
    host_id = models.IntegerField()
    snmp_query_id = models.IntegerField()
    snmp_index = models.CharField(max_length=255L)
    class Meta:
        db_table = 'data_local'

class DataTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    name = models.CharField(max_length=150L)
    class Meta:
        db_table = 'data_template'

class DataTemplateData(models.Model):
    id = models.IntegerField(primary_key=True)
    local_data_template_data_id = models.IntegerField()
    local_data_id = models.IntegerField()
    data_template_id = models.IntegerField()
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

class DataTemplateDataRra(models.Model):
    data_template_data_id = models.IntegerField()
    rra_id = models.IntegerField()
    class Meta:
        db_table = 'data_template_data_rra'

class DataTemplateRrd(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    local_data_template_rrd_id = models.IntegerField()
    local_data_id = models.IntegerField()
    data_template_id = models.IntegerField()
    t_rrd_maximum = models.CharField(max_length=2L, blank=True)
    rrd_maximum = models.CharField(max_length=20L)
    t_rrd_minimum = models.CharField(max_length=2L, blank=True)
    rrd_minimum = models.CharField(max_length=20L)
    t_rrd_heartbeat = models.CharField(max_length=2L, blank=True)
    rrd_heartbeat = models.IntegerField()
    t_data_source_type_id = models.CharField(max_length=2L, blank=True)
    data_source_type_id = models.IntegerField()
    t_data_source_name = models.CharField(max_length=2L, blank=True)
    data_source_name = models.CharField(max_length=19L)
    t_data_input_field_id = models.CharField(max_length=2L, blank=True)
    data_input_field_id = models.IntegerField()
    class Meta:
        db_table = 'data_template_rrd'

class GraphLocal(models.Model):
    id = models.IntegerField(primary_key=True)
    graph_template_id = models.IntegerField()
    host_id = models.IntegerField()
    snmp_query_id = models.IntegerField()
    snmp_index = models.CharField(max_length=255L)
    class Meta:
        db_table = 'graph_local'

class GraphTemplateInput(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    graph_template_id = models.IntegerField()
    name = models.CharField(max_length=255L)
    description = models.TextField(blank=True)
    column_name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'graph_template_input'

class GraphTemplateInputDefs(models.Model):
    graph_template_input_id = models.IntegerField()
    graph_template_item_id = models.IntegerField()
    class Meta:
        db_table = 'graph_template_input_defs'

class GraphTemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'graph_templates'

class GraphTemplatesGprint(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    name = models.CharField(max_length=100L)
    gprint_text = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'graph_templates_gprint'

class GraphTemplatesGraph(models.Model):
    id = models.IntegerField(primary_key=True)
    local_graph_template_graph_id = models.IntegerField()
    local_graph_id = models.IntegerField()
    graph_template_id = models.IntegerField()
    t_image_format_id = models.CharField(max_length=2L, blank=True)
    image_format_id = models.IntegerField()
    t_title = models.CharField(max_length=2L, blank=True)
    title = models.CharField(max_length=255L)
    title_cache = models.CharField(max_length=255L)
    t_height = models.CharField(max_length=2L, blank=True)
    height = models.IntegerField()
    t_width = models.CharField(max_length=2L, blank=True)
    width = models.IntegerField()
    t_upper_limit = models.CharField(max_length=2L, blank=True)
    upper_limit = models.CharField(max_length=20L)
    t_lower_limit = models.CharField(max_length=2L, blank=True)
    lower_limit = models.CharField(max_length=20L)
    t_vertical_label = models.CharField(max_length=2L, blank=True)
    vertical_label = models.CharField(max_length=200L, blank=True)
    t_slope_mode = models.CharField(max_length=2L, blank=True)
    slope_mode = models.CharField(max_length=2L, blank=True)
    t_auto_scale = models.CharField(max_length=2L, blank=True)
    auto_scale = models.CharField(max_length=2L, blank=True)
    t_auto_scale_opts = models.CharField(max_length=2L, blank=True)
    auto_scale_opts = models.IntegerField()
    t_auto_scale_log = models.CharField(max_length=2L, blank=True)
    auto_scale_log = models.CharField(max_length=2L, blank=True)
    t_scale_log_units = models.CharField(max_length=2L, blank=True)
    scale_log_units = models.CharField(max_length=2L, blank=True)
    t_auto_scale_rigid = models.CharField(max_length=2L, blank=True)
    auto_scale_rigid = models.CharField(max_length=2L, blank=True)
    t_auto_padding = models.CharField(max_length=2L, blank=True)
    auto_padding = models.CharField(max_length=2L, blank=True)
    t_base_value = models.CharField(max_length=2L, blank=True)
    base_value = models.IntegerField()
    t_grouping = models.CharField(max_length=2L, blank=True)
    grouping = models.CharField(max_length=2L)
    t_export = models.CharField(max_length=2L, blank=True)
    export = models.CharField(max_length=2L, blank=True)
    t_unit_value = models.CharField(max_length=2L, blank=True)
    unit_value = models.CharField(max_length=20L, blank=True)
    t_unit_exponent_value = models.CharField(max_length=2L, blank=True)
    unit_exponent_value = models.CharField(max_length=5L)
    class Meta:
        db_table = 'graph_templates_graph'

class GraphTemplatesItem(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    local_graph_template_item_id = models.IntegerField()
    local_graph_id = models.IntegerField()
    graph_template_id = models.IntegerField()
    task_item_id = models.IntegerField()
    color_id = models.IntegerField()
    alpha = models.CharField(max_length=2L, blank=True)
    graph_type_id = models.IntegerField()
    cdef_id = models.IntegerField()
    consolidation_function_id = models.IntegerField()
    text_format = models.CharField(max_length=255L, blank=True)
    value = models.CharField(max_length=255L, blank=True)
    hard_return = models.CharField(max_length=2L, blank=True)
    gprint_id = models.IntegerField()
    sequence = models.IntegerField()
    class Meta:
        db_table = 'graph_templates_item'

class GraphTree(models.Model):
    id = models.IntegerField(primary_key=True)
    sort_type = models.IntegerField()
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'graph_tree'

class GraphTreeItems(models.Model):
    id = models.IntegerField(primary_key=True)
    graph_tree_id = models.IntegerField()
    local_graph_id = models.IntegerField()
    rra_id = models.IntegerField()
    title = models.CharField(max_length=255L, blank=True)
    host_id = models.IntegerField()
    order_key = models.CharField(max_length=100L)
    host_grouping_type = models.IntegerField()
    sort_children_type = models.IntegerField()
    class Meta:
        db_table = 'graph_tree_items'

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

class HostGraph(models.Model):
    host_id = models.IntegerField()
    graph_template_id = models.IntegerField()
    class Meta:
        db_table = 'host_graph'

class HostSnmpCache(models.Model):
    host_id = models.IntegerField()
    snmp_query_id = models.IntegerField()
    field_name = models.CharField(max_length=50L)
    field_value = models.CharField(max_length=255L, blank=True)
    snmp_index = models.CharField(max_length=255L)
    oid = models.TextField()
    present = models.IntegerField()
    class Meta:
        db_table = 'host_snmp_cache'

class HostSnmpQuery(models.Model):
    host_id = models.IntegerField()
    snmp_query_id = models.IntegerField()
    sort_field = models.CharField(max_length=50L)
    title_format = models.CharField(max_length=50L)
    reindex_method = models.IntegerField()
    class Meta:
        db_table = 'host_snmp_query'

class HostTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    name = models.CharField(max_length=100L)
    class Meta:
        db_table = 'host_template'

class HostTemplateGraph(models.Model):
    host_template_id = models.IntegerField()
    graph_template_id = models.IntegerField()
    class Meta:
        db_table = 'host_template_graph'

class HostTemplateSnmpQuery(models.Model):
    host_template_id = models.IntegerField()
    snmp_query_id = models.IntegerField()
    class Meta:
        db_table = 'host_template_snmp_query'

class PluginAggregateColorTemplateItems(models.Model):
    color_template_item_id = models.IntegerField(primary_key=True)
    color_template_id = models.IntegerField()
    color_id = models.IntegerField()
    sequence = models.IntegerField()
    class Meta:
        db_table = 'plugin_aggregate_color_template_items'

class PluginAggregateColorTemplates(models.Model):
    color_template_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'plugin_aggregate_color_templates'

class PluginConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    directory = models.CharField(max_length=32L)
    name = models.CharField(max_length=64L)
    status = models.IntegerField()
    author = models.CharField(max_length=64L)
    webpage = models.CharField(max_length=255L)
    version = models.CharField(max_length=8L)
    class Meta:
        db_table = 'plugin_config'

class PluginDbChanges(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin = models.CharField(max_length=16L)
    table = models.CharField(max_length=64L)
    column = models.CharField(max_length=64L)
    method = models.CharField(max_length=16L)
    class Meta:
        db_table = 'plugin_db_changes'

class PluginFix64Bit(models.Model):
    local_data_id = models.IntegerField()
    rrd_maximum = models.CharField(max_length=19L)
    class Meta:
        db_table = 'plugin_fix64bit'

class PluginHooks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32L)
    hook = models.CharField(max_length=64L)
    file = models.CharField(max_length=255L)
    function = models.CharField(max_length=128L)
    status = models.IntegerField()
    class Meta:
        db_table = 'plugin_hooks'

class PluginNotificationLists(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128L)
    description = models.CharField(max_length=512L)
    emails = models.CharField(max_length=512L)
    class Meta:
        db_table = 'plugin_notification_lists'

class PluginRealms(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin = models.CharField(max_length=32L)
    file = models.TextField()
    display = models.CharField(max_length=64L)
    class Meta:
        db_table = 'plugin_realms'

class PluginRrdclean(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    last_mod = models.DateTimeField()
    size = models.CharField(max_length=255L)
    name_cache = models.CharField(max_length=255L)
    local_data_id = models.IntegerField()
    data_template_id = models.IntegerField()
    data_template_name = models.CharField(max_length=150L)
    class Meta:
        db_table = 'plugin_rrdclean'

class PluginRrdcleanAction(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    local_data_id = models.IntegerField()
    action = models.IntegerField()
    class Meta:
        db_table = 'plugin_rrdclean_action'

class PluginTholdContacts(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    type = models.CharField(max_length=32L)
    data = models.TextField()
    class Meta:
        db_table = 'plugin_thold_contacts'

class PluginTholdHostFailed(models.Model):
    id = models.IntegerField(primary_key=True)
    host_id = models.IntegerField()
    class Meta:
        db_table = 'plugin_thold_host_failed'

class PluginTholdLog(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.IntegerField()
    host_id = models.IntegerField()
    graph_id = models.IntegerField()
    threshold_id = models.IntegerField()
    threshold_value = models.CharField(max_length=64L)
    current = models.CharField(max_length=64L)
    status = models.IntegerField()
    type = models.IntegerField()
    description = models.CharField(max_length=255L)
    class Meta:
        db_table = 'plugin_thold_log'

class PluginTholdTemplateContact(models.Model):
    template_id = models.IntegerField()
    contact_id = models.IntegerField()
    class Meta:
        db_table = 'plugin_thold_template_contact'

class PluginTholdThresholdContact(models.Model):
    thold_id = models.IntegerField()
    contact_id = models.IntegerField()
    class Meta:
        db_table = 'plugin_thold_threshold_contact'

class Poller(models.Model):
    id = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=250L)
    ip_address = models.IntegerField()
    last_update = models.DateTimeField()
    class Meta:
        db_table = 'poller'

class PollerCommand(models.Model):
    poller_id = models.IntegerField()
    time = models.DateTimeField()
    action = models.IntegerField()
    command = models.CharField(max_length=200L)
    class Meta:
        db_table = 'poller_command'

class PollerItem(models.Model):
    local_data_id = models.IntegerField()
    poller_id = models.IntegerField()
    host_id = models.IntegerField()
    action = models.IntegerField()
    present = models.IntegerField()
    hostname = models.CharField(max_length=250L)
    snmp_community = models.CharField(max_length=100L)
    snmp_version = models.IntegerField()
    snmp_username = models.CharField(max_length=50L)
    snmp_password = models.CharField(max_length=50L)
    snmp_auth_protocol = models.CharField(max_length=5L)
    snmp_priv_passphrase = models.CharField(max_length=200L)
    snmp_priv_protocol = models.CharField(max_length=6L)
    snmp_context = models.CharField(max_length=64L, blank=True)
    snmp_port = models.IntegerField()
    snmp_timeout = models.IntegerField()
    rrd_name = models.CharField(max_length=19L)
    rrd_path = models.CharField(max_length=255L)
    rrd_num = models.IntegerField()
    rrd_step = models.IntegerField()
    rrd_next_step = models.IntegerField()
    arg1 = models.TextField(blank=True)
    arg2 = models.CharField(max_length=255L, blank=True)
    arg3 = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'poller_item'

class PollerOutput(models.Model):
    local_data_id = models.IntegerField()
    rrd_name = models.CharField(max_length=19L)
    time = models.DateTimeField()
    output = models.TextField()
    class Meta:
        db_table = 'poller_output'

class PollerOutputRt(models.Model):
    local_data_id = models.IntegerField()
    rrd_name = models.CharField(max_length=19L)
    time = models.DateTimeField()
    output = models.TextField()
    poller_id = models.IntegerField()
    class Meta:
        db_table = 'poller_output_rt'

class PollerReindex(models.Model):
    host_id = models.IntegerField()
    data_query_id = models.IntegerField()
    action = models.IntegerField()
    present = models.IntegerField()
    op = models.CharField(max_length=1L)
    assert_value = models.CharField(max_length=100L)
    arg1 = models.CharField(max_length=255L)
    class Meta:
        db_table = 'poller_reindex'

class PollerTime(models.Model):
    id = models.IntegerField(primary_key=True)
    pid = models.IntegerField()
    poller_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    class Meta:
        db_table = 'poller_time'

class Rra(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    name = models.CharField(max_length=100L)
    x_files_factor = models.FloatField()
    steps = models.IntegerField(null=True, blank=True)
    rows = models.IntegerField()
    timespan = models.IntegerField()
    class Meta:
        db_table = 'rra'

class RraCf(models.Model):
    rra_id = models.IntegerField()
    consolidation_function_id = models.IntegerField()
    class Meta:
        db_table = 'rra_cf'

class Settings(models.Model):
    name = models.CharField(max_length=50L, primary_key=True)
    value = models.CharField(max_length=1024L)
    class Meta:
        db_table = 'settings'

class SettingsGraphs(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50L)
    value = models.CharField(max_length=255L)
    class Meta:
        db_table = 'settings_graphs'

class SettingsTree(models.Model):
    user_id = models.IntegerField()
    graph_tree_item_id = models.IntegerField()
    status = models.IntegerField()
    class Meta:
        db_table = 'settings_tree'

class SnmpQuery(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    xml_path = models.CharField(max_length=255L)
    name = models.CharField(max_length=100L)
    description = models.CharField(max_length=255L, blank=True)
    graph_template_id = models.IntegerField()
    data_input_id = models.IntegerField()
    class Meta:
        db_table = 'snmp_query'

class SnmpQueryGraph(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    snmp_query_id = models.IntegerField()
    name = models.CharField(max_length=100L)
    graph_template_id = models.IntegerField()
    class Meta:
        db_table = 'snmp_query_graph'

class SnmpQueryGraphRrd(models.Model):
    snmp_query_graph_id = models.IntegerField()
    data_template_id = models.IntegerField()
    data_template_rrd_id = models.IntegerField()
    snmp_field_name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'snmp_query_graph_rrd'

class SnmpQueryGraphRrdSv(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    snmp_query_graph_id = models.IntegerField()
    data_template_id = models.IntegerField()
    sequence = models.IntegerField()
    field_name = models.CharField(max_length=100L)
    text = models.CharField(max_length=255L)
    class Meta:
        db_table = 'snmp_query_graph_rrd_sv'

class SnmpQueryGraphSv(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=32L)
    snmp_query_graph_id = models.IntegerField()
    sequence = models.IntegerField()
    field_name = models.CharField(max_length=100L)
    text = models.CharField(max_length=255L)
    class Meta:
        db_table = 'snmp_query_graph_sv'

class TholdData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150L, blank=True)
    rra_id = models.IntegerField()
    data_id = models.IntegerField()
    graph_id = models.IntegerField()
    graph_template = models.IntegerField()
    data_template = models.IntegerField()
    thold_hi = models.CharField(max_length=100L, blank=True)
    thold_low = models.CharField(max_length=100L, blank=True)
    thold_fail_trigger = models.IntegerField(null=True, blank=True)
    thold_fail_count = models.IntegerField()
    time_hi = models.CharField(max_length=100L, blank=True)
    time_low = models.CharField(max_length=100L, blank=True)
    time_fail_trigger = models.IntegerField()
    time_fail_length = models.IntegerField()
    thold_warning_hi = models.CharField(max_length=100L, blank=True)
    thold_warning_low = models.CharField(max_length=100L, blank=True)
    thold_warning_fail_trigger = models.IntegerField(null=True, blank=True)
    thold_warning_fail_count = models.IntegerField()
    time_warning_hi = models.CharField(max_length=100L, blank=True)
    time_warning_low = models.CharField(max_length=100L, blank=True)
    time_warning_fail_trigger = models.IntegerField()
    time_warning_fail_length = models.IntegerField()
    thold_alert = models.IntegerField()
    thold_enabled = models.CharField(max_length=3L)
    thold_type = models.IntegerField()
    bl_ref_time_range = models.IntegerField(null=True, blank=True)
    bl_pct_down = models.CharField(max_length=100L, blank=True)
    bl_pct_up = models.CharField(max_length=100L, blank=True)
    bl_fail_trigger = models.IntegerField(null=True, blank=True)
    bl_fail_count = models.IntegerField(null=True, blank=True)
    bl_alert = models.IntegerField()
    lastread = models.CharField(max_length=100L, blank=True)
    lasttime = models.DateTimeField()
    oldvalue = models.CharField(max_length=100L, blank=True)
    repeat_alert = models.IntegerField(null=True, blank=True)
    notify_default = models.CharField(max_length=3L, blank=True)
    notify_extra = models.TextField(blank=True)
    notify_warning_extra = models.CharField(max_length=512L, blank=True)
    notify_warning = models.IntegerField(null=True, blank=True)
    notify_alert = models.IntegerField(null=True, blank=True)
    host_id = models.IntegerField(null=True, blank=True)
    syslog_priority = models.IntegerField()
    data_type = models.IntegerField()
    cdef = models.IntegerField()
    percent_ds = models.CharField(max_length=64L)
    expression = models.CharField(max_length=70L)
    template = models.IntegerField()
    template_enabled = models.CharField(max_length=3L)
    tcheck = models.IntegerField()
    exempt = models.CharField(max_length=3L)
    restored_alert = models.CharField(max_length=3L)
    bl_thold_valid = models.IntegerField()
    class Meta:
        db_table = 'thold_data'

class TholdTemplate(models.Model):
    id = models.IntegerField()
    hash = models.CharField(max_length=32L)
    name = models.CharField(max_length=100L)
    data_template_id = models.IntegerField()
    data_template_name = models.CharField(max_length=100L)
    data_source_id = models.IntegerField()
    data_source_name = models.CharField(max_length=100L)
    data_source_friendly = models.CharField(max_length=100L)
    thold_hi = models.CharField(max_length=100L, blank=True)
    thold_low = models.CharField(max_length=100L, blank=True)
    thold_fail_trigger = models.IntegerField(null=True, blank=True)
    time_hi = models.CharField(max_length=100L, blank=True)
    time_low = models.CharField(max_length=100L, blank=True)
    time_fail_trigger = models.IntegerField()
    time_fail_length = models.IntegerField()
    thold_warning_hi = models.CharField(max_length=100L, blank=True)
    thold_warning_low = models.CharField(max_length=100L, blank=True)
    thold_warning_fail_trigger = models.IntegerField(null=True, blank=True)
    thold_warning_fail_count = models.IntegerField()
    time_warning_hi = models.CharField(max_length=100L, blank=True)
    time_warning_low = models.CharField(max_length=100L, blank=True)
    time_warning_fail_trigger = models.IntegerField()
    time_warning_fail_length = models.IntegerField()
    thold_enabled = models.CharField(max_length=3L)
    thold_type = models.IntegerField()
    bl_ref_time_range = models.IntegerField(null=True, blank=True)
    bl_pct_down = models.CharField(max_length=100L, blank=True)
    bl_pct_up = models.CharField(max_length=100L, blank=True)
    bl_fail_trigger = models.IntegerField(null=True, blank=True)
    bl_fail_count = models.IntegerField(null=True, blank=True)
    bl_alert = models.IntegerField()
    repeat_alert = models.IntegerField(null=True, blank=True)
    notify_default = models.CharField(max_length=3L, blank=True)
    notify_extra = models.TextField(blank=True)
    notify_warning_extra = models.CharField(max_length=512L, blank=True)
    notify_warning = models.IntegerField(null=True, blank=True)
    notify_alert = models.IntegerField(null=True, blank=True)
    data_type = models.IntegerField()
    cdef = models.IntegerField()
    percent_ds = models.CharField(max_length=64L)
    expression = models.CharField(max_length=70L)
    exempt = models.CharField(max_length=3L)
    restored_alert = models.CharField(max_length=3L)
    class Meta:
        db_table = 'thold_template'

class UserAuth(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50L)
    password = models.CharField(max_length=50L)
    realm = models.IntegerField()
    full_name = models.CharField(max_length=100L, blank=True)
    must_change_password = models.CharField(max_length=2L, blank=True)
    show_tree = models.CharField(max_length=2L, blank=True)
    show_list = models.CharField(max_length=2L, blank=True)
    show_preview = models.CharField(max_length=2L)
    graph_settings = models.CharField(max_length=2L, blank=True)
    login_opts = models.IntegerField()
    policy_graphs = models.IntegerField()
    policy_trees = models.IntegerField()
    policy_hosts = models.IntegerField()
    policy_graph_templates = models.IntegerField()
    enabled = models.CharField(max_length=2L)
    class Meta:
        db_table = 'user_auth'

class UserAuthPerms(models.Model):
    user_id = models.IntegerField()
    item_id = models.IntegerField()
    type = models.IntegerField()
    class Meta:
        db_table = 'user_auth_perms'

class UserAuthRealm(models.Model):
    realm_id = models.IntegerField()
    user_id = models.IntegerField()
    class Meta:
        db_table = 'user_auth_realm'

class UserLog(models.Model):
    username = models.CharField(max_length=50L)
    user_id = models.IntegerField()
    time = models.DateTimeField()
    result = models.IntegerField()
    ip = models.CharField(max_length=40L)
    class Meta:
        db_table = 'user_log'

class Version(models.Model):
    cacti = models.CharField(max_length=20L, blank=True)
    class Meta:
        db_table = 'version'

