from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_consultant = models.BooleanField(default=False)

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.service} - {self.customer.username}"

