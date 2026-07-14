from django.db import models
from students.models import Student
from django.utils import timezone
import random



class Fee(models.Model):

    STATUS_CHOICES = [

        ("Paid", "Paid"),

        ("Partial", "Partial"),

        ("Pending", "Pending"),

    ]



    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="fees",

    )



    term = models.CharField(

        max_length=20

    )



    year = models.PositiveIntegerField()



    amount = models.DecimalField(

        max_digits=10,

        decimal_places=2,

    )



    amount_paid = models.DecimalField(

        max_digits=10,

        decimal_places=2,

        default=0,

    )



    balance = models.DecimalField(

        max_digits=10,

        decimal_places=2,

        default=0,

    )



    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="Pending",

    )



    created_at = models.DateTimeField(

        auto_now_add=True

    )





    def update_balance(self):


        total_paid = sum(

            payment.amount

            for payment in self.payments.all()

        )



        self.amount_paid = total_paid



        self.balance = self.amount - total_paid





        if self.balance <= 0:


            self.status = "Paid"



        elif total_paid > 0:


            self.status = "Partial"



        else:


            self.status = "Pending"





        super().save(

            update_fields=[

                "amount_paid",

                "balance",

                "status",

            ]

        )





    def __str__(self):

        return f"{self.student} - {self.term} {self.year}"









class Payment(models.Model):


    PAYMENT_METHODS = [


        ("Cash", "Cash"),


        ("MPESA", "MPESA"),


        ("Bank", "Bank"),


    ]





    fee = models.ForeignKey(


        Fee,


        on_delete=models.CASCADE,


        related_name="payments"


    )





    amount = models.DecimalField(


        max_digits=10,


        decimal_places=2


    )





    receipt_number = models.CharField(


        max_length=20,


        unique=True,


        blank=True


    )





    method = models.CharField(


        max_length=20,


        choices=PAYMENT_METHODS,


        default="Cash"


    )





    payment_date = models.DateTimeField(


        default=timezone.now


    )





    created_at = models.DateTimeField(


        auto_now_add=True


    )








    def save(self, *args, **kwargs):


        if not self.receipt_number:


            self.receipt_number = (

                "REC"

                +

                str(
                    random.randint(
                        100000,
                        999999
                    )
                )

            )



        super().save(
            *args,
            **kwargs
        )



        self.fee.update_balance()









    def delete(self, *args, **kwargs):


        fee = self.fee



        super().delete(
            *args,
            **kwargs
        )



        fee.update_balance()







    def __str__(self):

        return f"{self.fee.student} - {self.amount}"