from django.db import models

# Create your models here.
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_age = models.IntegerField()
    patient_address = models.TextField()
    patient_gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
    patient_phone = models.CharField(max_length=15)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    recent_report = models.FileField(upload_to='appointment_reports', blank=True, null=True)
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date} {self.appointment_time}"
