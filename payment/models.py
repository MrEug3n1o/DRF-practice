from django.db import models
from borrowing.models import Borrowing

class Payment(models.Model):
    PENDING = "PENDING"
    PAID = "PAID"
    PAYMENT = "PAYMENT"
    FINE = "FINE"

    STATUS_CHOICES = [(PENDING, "Pending"), (PAID, "Paid")]
    TYPE_CHOICES = [(PAYMENT, "Payment"), (FINE, "Fine")]

    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE)

    session_url = models.URLField()
    session_id = models.CharField(max_length=255)
    money_to_pay = models.DecimalField(max_digits=7, decimal_places=2)
