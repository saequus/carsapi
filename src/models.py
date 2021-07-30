from django.contrib.auth.models import User
from django.db import models


def between_one_and_five(x: int):
    if not 1 <= x <= 5:
        raise ValueError("Value has to be between 1 and 5")


class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.model} ({self.make})"


class Rate(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(
        validators=[between_one_and_five], null=False, blank=False
    )

    def __str__(self):
        return f"Rate {self.id} with rating {self.rating} for {self.car.model}"
