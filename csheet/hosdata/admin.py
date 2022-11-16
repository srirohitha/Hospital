from django.contrib import admin
from .models import patientdetails
from .models import admissiondetails

admin.site.register(patientdetails)
admin.site.register(admissiondetails)

# Register your models here.
