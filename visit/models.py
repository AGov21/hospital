from datetime import timedelta
from django.db import models
from doctor.models import Doctor
from patient.models import Patient
from service.models import Service



class Visit(models.Model):
    PLANNED = 'PLANNED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (PLANNED, 'Запланирован'),
        (COMPLETED, 'Завершен'),
        (CANCELLED, 'Отменен'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visits')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    visit_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=0)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
   

    def __str__(self):
        return f'Врач: {self.doctor}, Пациент: {self.patient}'
    


