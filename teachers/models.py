from django.db import models
from classes.models import SchoolClass



class Teacher(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    employee_number = models.CharField(
        max_length=20,
        unique=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    SchoolClass = models.ForeignKey(
    SchoolClass,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
    )

    def __str__(self):
        return f"{self.employee_number} - {self.first_name} {self.last_name}"

# Create your models here.


# Create your models here.
