from datetime import timedelta
from django.db import models



class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField(default=timedelta(minutes=20))

    def __str__(self):
        return f'{self.name} - {self.price} тенге'