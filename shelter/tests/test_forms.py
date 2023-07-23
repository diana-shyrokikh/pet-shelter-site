from django.test import TestCase

from shelter.forms import PetOwnerCreationForm, PetOwnerUpdateForm


class FormsTests(TestCase):

    def test_pet_owner_creating_with_additional_inf(self):
        form_data = {
            "username": "new_user",
            "password1": "user123456",
            "password2": "user123456",
            "phone_number": "3 80 888 88 88",
            "first_name": "UserFirst",
            "last_name": "UserLast",
            "email": "test@test.com"

        }

        form = PetOwnerCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, form_data)

    def test_pet_owner_updating(self):
        form_data = {
            "phone_number": "3 80 888 88 88",
            "email": "test@test.com"
        }

        form = PetOwnerUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, form_data)
