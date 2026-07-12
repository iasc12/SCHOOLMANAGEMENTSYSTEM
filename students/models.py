from django.db import models
from classes.models import SchoolClass
from accounts.models import CustomUser


class Student(models.Model):

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="student_profile"
    )

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    phone_number = models.CharField(
        max_length=20
    )

    admission_number = models.CharField(
        max_length=20,
        unique=True
    )

    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # Student passport photo
    photo = models.ImageField(
        upload_to="student_photos/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.admission_number} - {self.first_name} {self.last_name}"