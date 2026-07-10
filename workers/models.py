from django.db import models

class Worker(models.Model):

    JOB_CHOICES = [
        ('Accountant', 'Accountant'),
        ('Cleaner', 'Cleaner'),
        ('Librarian', 'Librarian'),
        ('Driver', 'Driver'),
        ('security', 'Security'),
        ('Cook', 'Cook'),
        ('Nurse', 'Nurse'),
        ('Bursar', 'Bursar'),
    ]
    job = models.CharField(
        max_length=50,
        choices=JOB_CHOICES,
        default='nurse'
    )

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    # max_length=20,
        #unique=True
    #)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    #Workers = models.ForeignKey(
    #Workers,
    #on_delete=models.SET_NULL,
   # null=True,
   # blank=True
    #)

    def __str__(self):
        return f"{self.staff_number} {self.first_name} - {self.job}"

# Create your models here.


# Create your models here.
