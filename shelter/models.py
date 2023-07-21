from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models


from pet_shelter_site import settings


class Type(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        unique=True
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
    GENDERS = [
        ("Female", "Female"),
        ("Male", "Male"),
    ]
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=63, choices=GENDERS)
    type = models.ForeignKey(
        to=Type,
        related_name="pets_type",
        on_delete=models.CASCADE,
    )
    breed = models.ForeignKey(
        to=Breed,
        related_name="pets_breed",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(50)]
    )
    description = models.TextField(null=True, blank=True)
    last_vet_visit = models.DateField(null=True, blank=True)
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


class PetOwner(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=63, unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "pet owner"
        verbose_name_plural = "pet owners"

        ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
