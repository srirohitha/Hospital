from django.db import models
import uuid
STATUS_CHOICES = (

    ('Primary','Admitted'),
    ('Discharged','Discharged'),
    ('Consultation','Consultation')
 )

class casesheet(models.Model):
    patient_id= models.UUIDField(primary_key=True, editable=False, unique=True, null=False, default = uuid.uuid4)
    department=models.CharField(max_length=50)
    patientName = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    doctorName = models.CharField(max_length=50)
    primaryCheck = models.CharField(max_length=3)
    Consultationfee = models.CharField(max_length=50)
    status = models.CharField(max_length=15,default='Primary',choices=STATUS_CHOICES)
    referance = models.CharField(max_length=50)

    def __str__(self):
        return self.patientName  

class finalcasesheet(models.Model):
    pat_id=models.ForeignKey(casesheet,default=uuid.uuid4, on_delete=models.CASCADE)
    patientName = models.CharField(max_length=50)
    doc=models.DateField()
    medicines = models.TextField()
    finalstatus = models.CharField(max_length=15,default='Primary',choices=STATUS_CHOICES)
    remarks= models.TextField()

    def __str__(self):
        return self.patientName+ ' ' +self.finalstatus

 