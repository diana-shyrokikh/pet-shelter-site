from django.contrib.auth import get_user_model
from django.test import TestCase

from shelter.models import Type, Breed, Pet


class ModelsTests(TestCase):
    def setUp(self):
        self.cat = Type.objects.create(
            name="Cat",
        )
        self.breed = Breed.objects.create(
            name="CatTestBreed",
            type=self.cat
        )

        self.pet = Pet.objects.create(
            name="TestPet",
            gender="Female",
            type=self.cat,
        )

    def test_type_str(self):
        self.assertEquals(str(self.cat), self.cat.name)

    def test_breed_str(self):
        self.assertEquals(str(self.breed), self.breed.name)

    def test_pet_str(self):
        self.assertEquals(
            str(self.pet),
            f"{self.pet.type.name}: {self.pet.name}"
        )

    def test_pet_owner_creation(self):
        username = "newtest"
        password = "usertest123456"
        first_name = "FirstNameTest"
        last_name = "LastNameTest"
        email = "test@test.com"
        phone_number = "3 80 88 888 88 99"

        new_pet_owner = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number
        )

        self.assertEquals(new_pet_owner.username, username)
        self.assertTrue(new_pet_owner.check_password(password))
        self.assertEquals(new_pet_owner.phone_number, phone_number)
        self.assertEquals(
            str(new_pet_owner),
            f"{new_pet_owner.username} "
            f"({new_pet_owner.first_name} {new_pet_owner.last_name})"
        )
