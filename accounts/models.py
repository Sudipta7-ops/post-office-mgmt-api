from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    employee_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=10, blank=True)
    
    ROLE_CHOICES = [
        ('abpm', 'Assistant Branch Post Master'),
        ('bpm', 'Branch Post Master'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='abpm')

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return f"{self.employee_id} - {self.get_full_name()}"

# Create your models here.
