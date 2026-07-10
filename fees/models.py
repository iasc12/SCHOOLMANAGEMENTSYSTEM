from django.db import models
from classes.models import SchoolClass

class FeeStructure(models.Model):
    TERM_CHOICES = [
        ('Term 1', 'Term 1'),
        ('Term 2', 'Term 2'),
        ('Term 3', 'Term 3'),
    ]
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE
    )

    term = models.CharField(
        max_length=10,
        choices=TERM_CHOICES,
    )
    tuition_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    transport_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    activity_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    exam_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    boarding_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    def total_fee(self):
        return (
            self.tuition_fee +
            self.activity_fee +
            self.boarding_fee +
            self.transport_fee +
            self.exam_fee
        )

    


    def __str__(self):
        return f"{self.school_class} - {self.term}"