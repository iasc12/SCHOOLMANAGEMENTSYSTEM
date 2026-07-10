from django.db import models
from classes.models import SchoolClass
from accounts.models import CustomUser

class Students(models.Model):
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='student_profile'
        )


    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    admission_number = models.CharField(max_length=20, unique=True)
    SchoolClass = models.ForeignKey(
    SchoolClass,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

    def __str__(self):
        return f"{self.admission_number} - {self.first_name} {self.last_name}"

# Create your models here.
