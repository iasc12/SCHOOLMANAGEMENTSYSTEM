from django import forms
from .models import Fee, Payment



class FeeForm(forms.ModelForm):

    class Meta:

        model = Fee

        fields = [
            "student",
            "term",
            "year",
            "amount",
        ]




class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = [
            "amount",
            "method",
        ]


        widgets = {

            "amount": forms.NumberInput(
                attrs={
                    "class":"form-control"
                }
            ),


            "method": forms.Select(
                attrs={
                    "class":"form-control"
                }
            )

        }