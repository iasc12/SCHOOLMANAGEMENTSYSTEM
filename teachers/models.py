from django.db import models
from accounts.models import CustomUser


class Teacher(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
        null=True,
        blank=True,
    )

    employee_number = models.CharField(
        max_length=20,
        unique=True,
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    classes = models.ManyToManyField(
        "classes.SchoolClass",
        blank=True,
        related_name="teachers",
    )

    photo = models.ImageField(
        upload_to="teachers/photos/",
        blank=True,
        null=True,
    )

    qualification = models.CharField(
        max_length=150,
        blank=True,
    )

    specialization = models.CharField(
        max_length=150,
        blank=True,
    )

    employment_date = models.DateField(
        blank=True,
        null=True,
    )

    address = models.TextField(
        blank=True,
    )

    is_class_teacher = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "first_name",
            "last_name",
        ]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.employee_number} - {self.full_name}"