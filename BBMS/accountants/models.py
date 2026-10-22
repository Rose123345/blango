from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMINISTRATOR = "ADMIN", "Administrator"
        MANAGER = "MANAGER", "Blood Bank Manager"
        LAB_TECHNICIAN = "LAB", "Lab Technician"
        NURSE = "NURSE", "Nurse / Phlebotomist"
        DONOR = "DONOR", "Donor"
        HOSPITAL = "HOSPITAL", "Hospital / Requester"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.DONOR,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
