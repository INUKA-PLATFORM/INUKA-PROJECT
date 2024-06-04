from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_student= models.BooleanField('Is student', default=False)
    is_donor = models.BooleanField('Is donor', default=False)
