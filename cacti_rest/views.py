from models import DataInput
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponseBadRequest, Http404
from rest_framework import status
import simplejson
from serializers import *

class DataInputList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        objs = DataInput.objects.all()
        serializer = DataInputSerializer(objs, many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        try:
            serializer = DataInputSerializer(data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, ex:
            
                return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )

class DataInputDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return DataInput.objects.get(pk=pk)
        except DataInput.DoesNotExist:
            raise Exception("Object not found")

    def get(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            serializer = DataInputSerializer(obj)
            return Response(serializer.data)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
    def put(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            serializer = DataInputSerializer(obj, data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
    def delete(self, request, pk, format=None):
        try:
            snippet = self.get_object(pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )

class DataInputFieldsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        objs = DataInputFields.objects.all()
        serializer = DataInputFieldsSerializer(objs, many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        try:
            serializer = DataInputFieldsSerializer(data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, ex:
            
                return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )

class DataInputFieldsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return DataInputFields.objects.get(pk=pk)
        except DataInputFields.DoesNotExist:
            raise Exception("Object not found")

    def get(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            serializer = DataInputFieldsSerializer(obj)
            return Response(serializer.data)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
    def put(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            serializer = DataInputSerializer(obj, data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
    def delete(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
            
        
class HostList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        objs = Host.objects.all()
        serializer = HostSerializer(objs, many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        try:
            serializer = HostSerializer(data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, ex:
            
                return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )

class HostDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Host.objects.get(pk=pk)
        except Host.DoesNotExist:
            raise Exception("Object not found")

    def get(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            serializer = HostSerializer(obj)
            return Response(serializer.data)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
    def put(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            serializer = HostSerializer(obj, data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
    def delete(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
class HostTemplateList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        objs = HostTemplate.objects.all()
        serializer = HostTemplateSerializer(objs, many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        try:
            serializer = HostTemplateSerializer(data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, ex:
            
                return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )

class HostTemplateDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return HostTemplate.objects.get(pk=pk)
        except HostTemplate.DoesNotExist:
            raise Exception("Object not found")

    def get(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            serializer = HostTemplateSerializer(obj)
            return Response(serializer.data)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
    def put(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            serializer = HostTemplateSerializer(obj, data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )
    def delete(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception, ex:
            return HttpResponseBadRequest(
                    content=simplejson.dumps({"errors": [str(ex), ]}),
                    content_type="application/json",
                )