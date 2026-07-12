from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject

        fields = [
            "name",
            "code",
            "teacher",
            "classes",
            "is_compulsory",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"}),
            "teacher": forms.Select(attrs={"class": "form-select"}),
            "classes": forms.SelectMultiple(attrs={"class": "form-select"}),
            "is_compulsory": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }