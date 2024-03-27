from django.core.validators import MinValueValidator
from django.db import models

from ExamPrep.profiles.models import Profile


# o	Description
# 	Text field, optional.
# o	Image URL
# 	URL field, required.
# o	Price
# 	Float field, required.
# 	The number of decimal places of the price should not be specified in the database.
# 	The price cannot be below 0.0.
# o	Owner
# 	A foreign key to the Profile model.
# 	Establishes a many-to-one relationship with the Profile model, associating each album with a profile.
# 	The ON DELETE constraint must be configured to an appropriate value in alignment with the specified additional tasks.
# 	This field should remain hidden in forms.

class Album(models.Model):
    GENRE_CHOICES = [
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    ]
    name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Album Name",
    )
    artist_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name="Artist",
    )
    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL",
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.0),
        )
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )