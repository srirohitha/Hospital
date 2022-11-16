from rest_framework import serializers
from .models import patientdetails
from .models import admissiondetails

class patientserializer(serializers.ModelSerializer):
    class Meta:
        model=patientdetails
        fields=['pat_id', 'pat_name','problem']

class admissionserializer(serializers.ModelSerializer):
    class Meta:
        model=admissiondetails
        fields=['pd' ,'doj']        