from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student= models.BooleanField('Is student', default=True)
    student_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    
class Donation(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)
    consent = models.BooleanField(default=False)

    def __str__(self):
        return f"Donation by {self.first_name} {self.last_name} on {self.date}"
