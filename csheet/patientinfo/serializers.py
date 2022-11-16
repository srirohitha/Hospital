from rest_framework import serializers
from .models import casesheet
from .models import finalcasesheet

class casesheetserializer(serializers.ModelSerializer):
    class Meta:
        model=casesheet
        fields=['patientName' , 'department','disease','doctorName','Consultationfee','status','referance']

class finalcasesheetserializer(serializers.ModelSerializer):
    class Meta:
        model=finalcasesheet
        fields=['id' , 'patientName' , 'doc','medicines','finalstatus','remarks']        