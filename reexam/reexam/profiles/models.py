from django.core.validators import MinLengthValidator
from django.db import models

from reexam.profiles.validators import validate_name_capital_letter


class Profile(models.Model):
    nickname = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[
            MinLengthValidator(2, "Nickname must be at least 2 chars long!"),
        ],
    )
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=[
            validate_name_capital_letter,
        ],
    )
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=[
            validate_name_capital_letter,
        ],
    )
    chef = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"