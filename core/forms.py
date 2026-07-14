from django import forms
from .models import School


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = [
            "name",
            "motto",
            "address",
            "phone",
            "email",
            "website",
            "principal",
            "logo",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "motto": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "website": forms.URLInput(attrs={"class": "form-control"}),
            "principal": forms.TextInput(attrs={"class": "form-control"}),
        }