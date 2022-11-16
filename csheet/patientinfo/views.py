from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import casesheet
from .models import finalcasesheet
from .serializers import casesheetserializer
from .serializers import finalcasesheetserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])

def casesheet_list(request):
    if request.method == 'GET':
        casesheets=casesheet.objects.all()
        cserializer=casesheetserializer(casesheets,many=True)
        return Response(cserializer.data)
    if request.method == 'POST':
        cserializer=casesheetserializer(data=request.data)
        if cserializer.is_valid():
            cserializer.save()
            return Response(cserializer.data,status=status.HTTP_201_CREATED)    
@api_view(['GET','PUT','DELETE'])
def cs_detail(request,id):

    try:
        case=casesheet.objects.get(pk=id)
    except casesheet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        cserializer=casesheetserializer(case)
        return Response(cserializer.data)
    elif request.method =='PUT':
        cserializer=casesheetserializer(case,data=request.data)
        if cserializer.is_valid():
            cserializer.save()
            return Response(cserializer.data)
        return Response(cserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        case.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):
    return HttpResponse("Welcome...")

@api_view(['GET','POST'])

def finalcasesheet_list(request):
    if request.method == 'GET':
        casesheets=finalcasesheet.objects.all()
        cserializer=finalcasesheetserializer(casesheets,many=True)
        return Response(cserializer.data)
    if request.method == 'POST':
        cserializer=finalcasesheetserializer(data=request.data)
        if cserializer.is_valid():
            cserializer.save()
            return Response(cserializer.data,status=status.HTTP_201_CREATED)    
@api_view(['GET','PUT','DELETE'])
def finalcs_detail(request,id):

    try:
        case=finalcasesheet.objects.get(pk=id)
    except finalcasesheet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        cserializer=finalcasesheetserializer(case)
        return Response(cserializer.data)
    elif request.method =='PUT':
        cserializer=finalcasesheetserializer(case,data=request.data)
        if cserializer.is_valid():
            cserializer.save()
            return Response(cserializer.data)
        return Response(cserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        case.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
