from django.db import models



from django.db import models


class Teacher(models.Model):
    employee_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    email = models.EmailField(blank=True)

    phone_number = models.CharField(max_length=15)

    department = models.CharField(max_length=100)

    qualification = models.CharField(max_length=100)

    date_hired = models.DateField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee_number} - {self.first_name} {self.last_name}"



# Create your models here.
