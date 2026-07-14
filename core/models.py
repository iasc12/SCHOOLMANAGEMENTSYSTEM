from django.db import models


class School(models.Model):

    name = models.CharField(max_length=200)

    motto = models.CharField(
        max_length=255,
        blank=True
    )

    address = models.TextField()

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField()

    website = models.URLField(
        blank=True
    )

    logo = models.ImageField(
        upload_to="school/logo/",
        blank=True,
        null=True
    )

    principal = models.CharField(
        max_length=200,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name