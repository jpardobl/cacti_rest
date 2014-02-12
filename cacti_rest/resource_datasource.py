#from django.views.decorators.csrf import csrf_exempt
from cacti_rest.utils import retrieve_param
from django.http import HttpResponseServerError
from django.shortcuts import render_to_response 
from cacti_rest.models import DataLocal, Settings, DataTemplateData
import logging, simplejson#, traceback
from cacti_rest.rra import extract_data, convert_to_json
from cacti_rest.settings import RRA_PATH
from django.core.urlresolvers import reverse

def get(request, id_ds):
    try:
        data = DataTemplateData.objects.get(local_data_id=id_ds)
        
        path = data.data_source_path.replace("<path_rra>", RRA_PATH)

        if "start" in request.GET and request.GET["start"] is not None: 
            start = request.GET["start"]
        else:
            start = "-1h"

        if path is None: 
            raise("Can't find data related to datasouce %s" % data)
        
        data = convert_to_json(extract_data(path, 300, start))
	        
        response =  render_to_response(
            "cacti_rest/json/datasource.json",
            {"data": data,
             "id": id_ds,
             "url": reverse("resource_datasource", args=[id_ds, ]),
            },
            content_type="application/json") 
        response['Cache-Control'] = 'no-cache'
        return response
    except Exception, ex:
        logging.error("Resource get error: %s" % ex)
        response =  HttpResponseServerError(
            content=simplejson.dumps({"errors": ex}),
            content_type="application/json") 
        response['Cache-Control'] = 'no-cache'
        return response
    
#@csrf_exempt
#@access_required
def entrance(request, *args, **kwargs):

    if request.method == "GET":
        return get(request, *args, **kwargs)

    
