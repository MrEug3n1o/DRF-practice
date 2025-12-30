from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)

    class CoverType(models.TextChoices):
        HARD = ("HARD", )
        SOFT = ("SOFT", )

    cover = models.CharField(
        max_length=4,
        choices=CoverType,
        default=CoverType.HARD
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ["title"]
