from datetime import datetime
from django.db import models
from specialization.models import Specialization
from analytic.models import Department
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='doctors')
    contact_info = models.CharField(max_length=124)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors', null=True)



    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return f'{self.full_name} - {self.specialization}'
    




class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье')
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.doctor} - {self.day_of_week}: {self.start_time} - {self.end_time}'



    