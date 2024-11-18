from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Notification(models.Model):
    NEW = 'NEW'
    READ = 'READ'
    ARCHIVED = 'ARCHIVED'

    STATUS_CHOICES = [
        (NEW, 'NEW'),
        (READ, 'READ'),
        (ARCHIVED, 'ARCHIVED')
    ]

    VISIT_CREATED = 'VISIT_CREATED'
    VISIT_CANCELLED = 'VISIT_CANCELLED'
    DOCTOR_DELETE = 'DOCTOR_DELETE'
    PATIENT_DELETE = 'PATIENT_DELETE'
    OTHER = 'OTHER'

    TYPE_CHOICES = [
        (VISIT_CREATED, 'VISIT_CREATED'),
        (VISIT_CANCELLED, 'VISIT_CANCELLED'),
        (OTHER, 'OTHER'),
        (DOCTOR_DELETE, 'DOCTOR_DELETE'),
        (PATIENT_DELETE, 'PATIENT_DELETE')
    ]

    sender = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_notifications', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=OTHER)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.recipient} : {self.message[:20]}'

    class Meta:
        ordering = ['-created_at']