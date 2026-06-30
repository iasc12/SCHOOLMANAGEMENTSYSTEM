from django.db import models


from django.db import models


class Student(models.Model):
    admission_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    date_of_birth = models.DateField()

    email = models.EmailField(blank=True)

    phone_number = models.CharField(max_length=15)

    address = models.TextField()

    date_admitted = models.DateField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.admission_number} - {self.first_name} {self.last_name}"


# Create your models here.
