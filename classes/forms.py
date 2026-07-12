from django import forms
from .models import SchoolClass


class SchoolClassForm(forms.ModelForm):

    class Meta:
        model = SchoolClass

        fields = [
            "name",
            "section",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Class Name",
                }
            ),
            "section": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Section",
                }
            ),
        }