from django import forms
from django.contrib.auth.forms import UserCreationForm

from shelter.models import Pet, Breed, PetOwner, Type


class BreedSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )
    type = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )


class CatForm(forms.ModelForm):
    breed = forms.ModelChoiceField(
        queryset=Breed.objects.filter(type__name="Cat"),
        required=False
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.filter(name="Cat"),
    )

    class Meta:
        model = Pet
        exclude = ("pet_owner", "left_at")


class CatSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )
    breed = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )
    gender = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )


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
        exclude = ("pet_owner", "left_at")


class DogSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )
    breed = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )
    gender = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )


class PetSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )
    breed = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )


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


class PetOwnerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )
    first_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput()
    )
