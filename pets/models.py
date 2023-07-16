from django.contrib.auth import get_user_model
from django.db import models


PET_KIND_CHOICES = (
    ("dog", "Dog"),
    ("cat", "Cat"),
    ("bird", "Bird"),
)

User = get_user_model()


class Pet(models.Model):
    """Model representing a pet."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=255,)
    kind = models.CharField(max_length=10, choices=PET_KIND_CHOICES,)
    photo = models.ImageField(
        upload_to="pets/images/",
        null=True,
        default=None,
    )

    def __str__(self):
        return self.name
