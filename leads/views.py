from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Lead
from .serializers import LeadSerializer


@api_view(['GET', 'POST'])
def lead_list_create(request):
    ''' list all the leads and create new lead '''
    if request.method == 'GET':
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def lead_detail(request, pk):
    ''' get, update and put  leads '''
    try:
        lead = Lead.objects.get(pk=pk)
    except Lead.DoesNotExist:
        data = {}
        data['message'] = 'Lead not found'
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeadSerializer(lead)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = LeadSerializer(
            instance=lead, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation = lead.delete()
        data = {}
        if operation:
            data["flag"] = "success"
            data["message"] = "Deleted successfully"
        else:
            data["flag"] = "danger"
            data['message'] = "Delete operation failed"
        return Response(data=data)
