from django.db import models
from django.conf import settings
from services.models import Service


class Appointment(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('booked', 'Booked'), (
        'completed', 'Completed'), ('cancelled', 'Cancelled')], default='booked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.customer} on {self.appointment_time}"
