from django.db import models


class SchoolClass(models.Model):

    name = models.CharField(
        max_length=50
    )

    stream = models.CharField(
        max_length=30
    )

    academic_year = models.PositiveIntegerField()

    teachers = models.ManyToManyField(
        'teachers.Teacher',
        related_name='classes',
        blank=True
    )

    def __str__(self):
        return f"{self.name} {self.stream} {self.academic_year}"