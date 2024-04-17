from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from reexam.profiles.models import Profile


class Recipe(models.Model):

    TYPE_CHOICES = (
        ("French", "French"),
        ("Chinese", "Chinese"),
        ("Italian", "Italian"),
        ("Balkan", "Balkan"),
        ("Other", "Other"),
    )

    title = models.CharField(
        max_length=100,
        unique=True,
        error_messages={'unique': "We already have a recipe with the same title!"},
        validators=[
            MinLengthValidator(10),

        ],
    )
    cuisine_type = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES,
    )
    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space.",
    )
    instructions = models.TextField(
        null=False,
        blank=False,
    )
    cooking_time = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1),
        ],
        help_text="Provide the cooking time in minutes.",
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title