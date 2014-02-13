#from django.views.decorators.csrf import csrf_exempt
from cacti_rest.utils import retrieve_param
from django.http import HttpResponseServerError
from django.shortcuts import render_to_response 
from cacti_rest.models import DataTemplateData, DataLocal
import logging, simplejson#, traceback
from cacti_rest.rra import extract_data, convert_to_json
from cacti_rest.settings import RRA_PATH
from django.core.urlresolvers import reverse

def get(request, id_ds):
    try:
        obj = DataTemplateData.objects.get(local_data_id=id_ds)
        
        path = obj.data_source_path.replace("<path_rra>", RRA_PATH)
        if path is None: 
            raise("Can't find data related to datasouce %s" % data)
        start = retrieve_param(request, "start", "-1h")        
        data = convert_to_json(extract_data(path, 300, start))
        response =  render_to_response(
            "cacti_rest/json/datasource.json",
            {
             "resource_type": "datasource",
             "data": data,
             "id": id_ds,
             "url": reverse("resource_datasource", args=[id_ds, ]),
             "host_resource": reverse("resource_host", args=[obj.local_data_id.host_id.id, ]),
            },
            content_type="application/json") 
        response['Cache-Control'] = 'no-cache'
        return response
    except Exception, ex:
        logging.error("Resource get error: %s" % ex)
        
        response =  HttpResponseServerError(
                content=simplejson.dumps({"errors": str(ex)}),                
                content_type="application/json") 
        
        response['Cache-Control'] = 'no-cache'
        return response
    
#@csrf_exempt
#@access_required
def entrance(request, *args, **kwargs):

    if request.method == "GET":
        return get(request, *args, **kwargs)

    
