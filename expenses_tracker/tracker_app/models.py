from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

# Create your models here.
from expenses_tracker.tracker_app.validators import only_letters_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=(
            only_letters_validator,
            MinLengthValidator(2),
        )
    )

    last_name = models.CharField(
        max_length=15,
        validators=(
            only_letters_validator,
            MinLengthValidator(2),
        )
    )

    budget = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(0.0),
        ]

    )

    image = models.ImageField(
        'Profile Image',
        upload_to='images/',
        default='expenses_tracker/static/images/user.png'

    )


class Expense(models.Model):
    title = models.CharField(
        'Title',
        max_length=30,
    )

    image = models.URLField(
        'Expense Image',
    )

    description = models.TextField(
        'Description',
        blank=True,
        null=True,
    )

    price = models.FloatField(
        'Price',
    )

    owner_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,

    )
