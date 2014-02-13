#from django.views.decorators.csrf import csrf_exempt
from cacti_rest.utils import retrieve_param
from django.http import HttpResponseServerError
from django.shortcuts import render_to_response 
from cacti_rest.models import Host
import logging, simplejson
from django.core.urlresolvers import reverse


def get(request):
    try:
        offset = int(retrieve_param(request, "offset", 0))
        limit = int(retrieve_param(request, "limit", 50)) + offset 
        #print "offset: %s; Limit: %s" % (offset, limit)
        data = [{"resource_type": "host", "url": reverse("resource_host", args=[x.id, ])} for x in Host.objects.all()[offset:limit]]
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

    