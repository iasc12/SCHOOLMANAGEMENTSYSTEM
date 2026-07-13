from django import forms
from .models import Worker


class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = [
            "employee_number",
            "first_name",
            "last_name",
            "gender",
            "phone",
            "job_title",
            "email",
        ]

        widgets = {
            "employee_number": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "first_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "last_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "gender": forms.Select(
                attrs={"class": "form-control"}
            ),

            "phone": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "job_title": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),
        }