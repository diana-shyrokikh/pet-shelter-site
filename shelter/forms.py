from django import forms
from django.contrib.auth.forms import UserCreationForm

from shelter.models import Pet, Breed, PetOwner, Type


class CatForm(forms.ModelForm):
    breed = forms.ModelChoiceField(
        queryset=Breed.objects.filter(type__name="Cat"),
        required=False
    )

    class Meta:
        model = Pet
        fields = "__all__"


class DogForm(forms.ModelForm):
    breed = forms.ModelChoiceField(
        queryset=Breed.objects.filter(type__name="Dog"),
        required=False
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.filter(name="Dog"),
    )

    class Meta:
        model = Pet
        fields = "__all__"


class PetOwnerCreationForm(UserCreationForm):
    class Meta:
        model = PetOwner
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "phone_number"
        )


class PetOwnerUpdateForm(forms.ModelForm):
    class Meta:
        model = PetOwner
        fields = ("email", "phone_number")
