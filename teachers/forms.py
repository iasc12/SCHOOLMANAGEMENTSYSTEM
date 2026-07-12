from django import forms
from .models import Teacher


class TeacherProfileForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = [
            'employee_number',
            'first_name',
            'last_name',
            'gender',
            'phone',
            'email',
        ]