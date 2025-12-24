from django.db import models
from borrowing.models import Borrowing

class Payment(models.Model):

    class PayStatus(models.TextChoices):
        PENDING = ("PENDING", )
        PAID = ("PAID", )

    class PayType(models.TextChoices):
        PAYMENT = ("PAYMENT", )
        FINE = ("FINE", )

    status = models.CharField(max_length=7, choices=PayStatus, default=PayStatus.PENDING)
    type = models.CharField(max_length=7, choices=PayType, default=PayType.PAYMENT)
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE)

    session_url = models.URLField()
    session_id = models.CharField(max_length=255)
    money_to_pay = models.DecimalField(max_digits=7, decimal_places=2)
