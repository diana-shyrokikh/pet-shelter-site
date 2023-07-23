from datetime import date
from typing import Any, Callable

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxValueValidator,
    RegexValidator
)
from django.db import models


from pet_shelter_site import settings


class Type(models.Model):
    TYPES = [
        ("Dog", "Dog"),
        ("Cat", "Cat"),
    ]

    name = models.CharField(
        max_length=63,
        unique=True,
        choices=TYPES
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Breed(models.Model):
    NAME_PATTERN = r"^[\sA-Za-z]+$"

    name = models.CharField(
        max_length=255,
        unique=True,
        default="unknown",
        validators=[
            RegexValidator(
                regex=NAME_PATTERN,
                message="The value must consist of A-z and a-z only"
            )
        ],
    )
    type = models.ForeignKey(
        to=Type,
        related_name="breeds",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["type", "name"]

    def __str__(self):
        return f"{self.name}"


class Pet(models.Model):
    NAME_PATTERN = r"^[\sA-Za-z]+$"

    GENDERS = [
        ("Female", "Female"),
        ("Male", "Male"),
    ]

    name = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=NAME_PATTERN,
                message="The value must consist of A-z and a-z only"
            )
        ],
    )
    gender = models.CharField(max_length=63, choices=GENDERS)
    type = models.ForeignKey(
        to=Type,
        related_name="pets_type",
        on_delete=models.CASCADE,
    )
    breed = models.ForeignKey(
        to=Breed,
        related_name="pets_breed",
        on_delete=models.SET_DEFAULT,
        blank=True,
        null=True,
        default=None
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(50)]
    )
    description = models.TextField(null=True, blank=True)
    arrived_at = models.DateField(auto_now_add=True)
    left_at = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")
    pet_owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="pets",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-arrived_at"]

    def __str__(self):
        return (
            f"{self.type.name}: {self.name}"
        )

    def clean(self) -> None:
        if self.left_at:
            if self.left_at > date.today():
                raise ValidationError(
                    message="The date must not be in the future"
                )

    def save(
            self,
            force_insert: bool = False,
            force_update: bool = False,
            using: Any = None,
            update_fields: Any = None
    ) -> Callable:
        self.full_clean()

        return super().save(
            force_insert,
            force_update,
            using,
            update_fields
        )


class PetOwner(AbstractUser):
    USERNAME_PATTERN = r"^[a-z\d_]+$"
    NAME_PATTERN = r"^[A-Za-z]+$"
    PHONE_NUMBER_PATTERN = r"^[\d\s()+]+$"

    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=USERNAME_PATTERN,
                message="The value must consist of a-z, digits and _ only"
            )
        ],
    )
    first_name = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=NAME_PATTERN,
                message="The value must consist of A-z and a-z only"
            )
        ],
    )
    last_name = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=NAME_PATTERN,
                message="The value should consist of A-z and a-z only"
            )
        ],
    )
    phone_number = models.CharField(
        max_length=63,
        unique=True,
        validators=[
            RegexValidator(
                regex=PHONE_NUMBER_PATTERN,
                message=(
                    "The value must consist of numbers and "
                    "allows parentheses with spaces and +"
                )
            )
        ],
    )
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "pet owner"
        verbose_name_plural = "pet owners"

        ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
