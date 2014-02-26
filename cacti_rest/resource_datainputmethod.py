from django.views.decorators.csrf import csrf_exempt
from cacti_rest.utils import retrieve_param, generate_hash
from django.http import HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect 
from cacti_rest.models import DataInput
import logging, simplejson
from django.core.urlresolvers import reverse
from cacti_rest.forms import DataInputForm

def get(request, *args, **kwargs):
    try:
        
        obj = DataInput.objects.get(id=args[0])
        response =  render_to_response(
            "cacti_rest/json/object.json",
            {"data": obj.to_json()},
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
    
    
def post(request, *args, **kwargs):
    
    try:
        
        form = DataInputForm(request.POST)
        
        if form.is_valid():
            
            obj = form.save(commit=False)
            
            obj.hash = str(generate_hash(request))
            obj.save()
            return redirect(reverse("resource_datainputmethod", args=[obj.id, ]))
        return HttpResponseBadRequest(
                content=simplejson.dumps({"errors": [form.errors, ]}),
                content_type="application/json",
                )
            
    except Exception, ex:
        logging.error("Resource creation error: %s" % ex)
        response =  HttpResponseServerError(
            content=simplejson.dumps({"errors": str(ex)}),
            content_type="application/json") 
        response['Cache-Control'] = 'no-cache'
        return response
    
@csrf_exempt
#@access_required
def entrance(request, *args, **kwargs):

    if request.method == "GET":
        return get(request, *args, **kwargs)
    if request.method == "POST":
        return post(request, *args, **kwargs)
    