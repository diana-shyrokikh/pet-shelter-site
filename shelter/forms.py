from django import forms

from shelter.models import Pet, Breed


class CatForm(forms.ModelForm):
    breed = forms.ModelChoiceField(
        queryset=Breed.objects.filter(type__name="Cat"),
        required=False
    )

    class Meta:
        model = Pet
        fields = "__all__"
