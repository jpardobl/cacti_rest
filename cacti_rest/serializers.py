from models import *

from rest_framework import serializers


class DataInputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataInput
        fields = ('id', 'name', 'type_id', 'input_string', 'output_fields',)
        

class DataInputFieldsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataInputFields
        fields = ('id', 'name', 'data_name', "data_input_id", "input_output", "update_rra")


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        #fields = ('id', 'name', 'data_name', "data_input_id", "input_output", "update_rra")
        
class HostTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HostTemplate