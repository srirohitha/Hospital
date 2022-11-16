from django.db import models
from django.core.validators import MinValueValidator


class patientdetails(models.Model):
    pat_id=models.IntegerField(primary_key=True,validators=[MinValueValidator(1)])
    pat_name=models.CharField(max_length=50)
    problem=models.CharField(max_length=100)

    def __str__(self):
        return str(self.pat_id)+' '+self.pat_name

class admissiondetails(models.Model):
    pd=models.ForeignKey(patientdetails, on_delete=models.CASCADE)
    doj=models.DateField(null=False)
    
    def __str__(self):
        return str(self.pd) +' '+str(self.doj)
    
