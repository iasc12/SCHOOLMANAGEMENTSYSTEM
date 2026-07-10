from django.db import models
from teachers.models import Teacher
from classes.models import SchoolClass




class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    SchoolClass = models.ForeignKey(
    SchoolClass,
    on_delete=models.CASCADE,
   # null=True,
    #blank=True
    )

    def __str__(self):
        return self.name

# Create your models here.
