from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True)
    is_company_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name