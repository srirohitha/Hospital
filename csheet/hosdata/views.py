from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import patientdetails
from .models import admissiondetails
from .serializers import patientserializer
from .serializers import admissionserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#def patcount(request,n):

@api_view(['GET','POST'])

def patient_list(request):
    if request.method == 'GET':
        patients=patientdetails.objects.all()
        pserializer=patientserializer(patients,many=True)
       # x = pserializer.data
       # p_name = x.get('pat_name')
        return Response(pserializer.data)
    if request.method == 'POST':
        pserializer=patientserializer(data=request.data)
        if pserializer.is_valid():
            pserializer.save()
           # x = pserializer.data
           #p_name = x.get('pat_name')
            return Response(pserializer.data,status=status.HTTP_201_CREATED)    
@api_view(['GET','PUT','DELETE'])
def patient_list_id(request,pat_id):

    try:
        details=patientdetails.objects.get(pk=pat_id)
    except patientdetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        pserializer=patientserializer(details)
        return Response(pserializer.data)
    elif request.method =='PUT':
        pserializer=patientserializer(details,data=request.data)
        if pserializer.is_valid():
            pserializer.save()
            return Response(pserializer.data)
        return Response(pserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):
    return HttpResponse("Welcome...")

@api_view(['GET','POST'])

def admission_list(request):
    if request.method == 'GET':
        details=admissiondetails.objects.all()
        aserializer=admissionserializer(details,many=True)
        return Response(aserializer.data)
    if request.method == 'POST':
        aserializer=admissionserializer(data=request.data)
        if aserializer.is_valid():
            aserializer.save()
            return Response(aserializer.data,status=status.HTTP_201_CREATED)    
@api_view(['GET','PUT','DELETE'])
def admission_list_id(request,id):

    try:
        details=admissiondetails.objects.get(pk=id)
    except admissiondetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        aserializer=admissionserializer(details,many=True)
        return Response(aserializer.data)
    elif request.method =='PUT':
        aserializer=admissionserializer(details,data=request.data)
        if aserializer.is_valid():
            aserializer.save()
            return Response(aserializer.data)
        return Response(aserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def patcount(request,n):
    cnt=0
    total=patientdetails.objects.count()
    lst=[]
    for idx in range(1,total):
        
        x = admissiondetails.objects.filter(pd__pat_id=idx).count()
        if x >= n:
            cnt += 1

            pname=patientdetails.objects.filter(pat_id=idx).values('pat_name')
            lst.append(pname[0]["pat_name"])
            lst.append(" ")
    
    #print(len(lst))
    #x=admissiondetails.objects.filter(pd__pat_id=n).count()
    return HttpResponse(lst)
    #return HttpResponse("No of patients admitted more than "+str(n)+" times are: " +str(cnt))
  
    # return HttpResponse("Patient with id "+str(n)+" is admitted "+str(x)+"times")

# Create your views here.
