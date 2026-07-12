from django.db import models

from teachers.models import Teacher
from classes.models import SchoolClass


class Subject(models.Model):

    name = models.CharField(
        max_length=100
    )

    code = models.CharField(
        max_length=20,
        unique=True
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    classes = models.ManyToManyField(
        SchoolClass,
        blank=True
    )

    is_compulsory = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.code} - {self.name}"