from django.forms import ModelForm
from cacti_rest.models import DataInput


class DataInputForm(ModelForm):
    class Meta:
        model = DataInput