from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser
from .models import Teacher


class TeacherProfileForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = [
            "employee_number",
            "first_name",
            "last_name",
            "gender",
            "phone",
            "email",
        ]


class AddTeacherForm(UserCreationForm):

    employee_number = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    gender = forms.ChoiceField(
        choices=Teacher.GENDER_CHOICES
    )

    phone = forms.CharField(max_length=20)

    email = forms.EmailField()

    class Meta:
        model = CustomUser

        fields = [
            "username",
            "password1",
            "password2",
        ]