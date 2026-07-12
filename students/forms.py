from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = [
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "phone_number",
            "admission_number",
            "school_class",
            "photo",
        ]

        widgets = {

            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "gender": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "admission_number": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "school_class": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "photo": forms.FileInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }