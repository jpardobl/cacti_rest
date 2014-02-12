#from django.views.decorators.csrf import csrf_exempt
from cacti_rest.utils import retrieve_param
from django.http import HttpResponseServerError
from django.shortcuts import render_to_response 
from cacti_rest.models import DataLocal, Settings
import logging, simplejson
from cacti_rest.rra import extract_data, convert_to_json

def get(request, id_ds):
    try:
        data = DataLocal.objects.get(id=id_ds)
        
        path = data.get_rra_path()
        resolution =  300
        start = "-1h"
        
        if path is None: logging.debug("El path del datasouce %s es None" % data)
        
        data = convert_to_json(extract_data(path, resolution, start))
        
        response =  render_to_response(
            "cacti_rest/json/list.json",
            {"data": data},
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

    