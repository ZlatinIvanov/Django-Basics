from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator
from django.db import models


def validate_username(value):
    is_valid = all(c.isalpha() or c.isdigit() or c == "_" for c in value)

    if not is_valid:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(15),
            validate_username,
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )
