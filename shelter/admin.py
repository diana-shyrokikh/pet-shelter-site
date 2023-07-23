from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from shelter.models import (
    Breed,
    Type,
    Pet,
    PetOwner
)


@admin.register(PetOwner)
class PetOwnerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("phone_number", "date_joined")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("phone_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "is_staff",)}),
    )
    list_filter = ["date_joined", "is_staff"]
    search_fields = ["last_name"]


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ["name", "type"]
    search_fields = ["name"]
    list_filter = ["type"]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "gender",
        "type",
        "breed",
        "age",
        "arrived_at",
        "pet_owner",
    ]
    list_filter = [
        "gender",
        "type",
        "breed",
        "age",
        "arrived_at",
        "left_at"
    ]
    raw_id_fields = ["breed"]
    search_fields = ["name"]
