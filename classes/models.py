from django.db import models


class SchoolClass(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )


    section = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        if self.section:
            return f"{self.name} {self.section}"

        return self.name