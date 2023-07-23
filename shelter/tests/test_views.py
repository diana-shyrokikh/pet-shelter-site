from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from shelter.models import Type, Pet, Breed

PK = "0"

ADOPT_PET = reverse("shelter:adopt-pet", args="1")
BREED_CREATE = reverse("shelter:breed-create")
BREED_UPDATE = reverse("shelter:breed-update", args="1")
DOG_CREATE = reverse("shelter:dog-create")
DOG_UPDATE = reverse("shelter:dog-update", args="1")
CAT_CREATE = reverse("shelter:cat-create")
CAT_UPDATE = reverse("shelter:cat-update", args="2")
PET_LIST = reverse("shelter:pet-list")
PET_OWNER_LIST = reverse("shelter:pet-owner-list")
PET_OWNER_CREATE = reverse("shelter:pet-owner-create")


class PublicViewsTests(TestCase):
    def setUp(self) -> None:
        self.pet_owner = get_user_model().objects.create_user(
            username="test",
            password="usertest123456",
            first_name="FirstName",
            last_name="LastName",
            email="test@test.com",
            phone_number="3 80 88 888 88 89"
        )

        self.client.force_login(self.pet_owner)

        self.dog = Type.objects.create(
            name="Dog",
        )

        Pet.objects.create(
            name="TestDog",
            gender="Female",
            type=self.dog,
        )

        self.cat = Type.objects.create(
            name="Cat",
        )

        Pet.objects.create(
            name="TestCat",
            gender="Female",
            type=self.cat,
        )

    def test_adop_pet_staff_required(self):
        response = self.client.get(ADOPT_PET)

        self.assertNotEquals(response.status_code, 200)

    def test_breed_create_staff_required(self):
        response = self.client.get(BREED_CREATE)

        self.assertNotEquals(response.status_code, 200)

    def test_breed_update_staff_required(self):
        response = self.client.get(BREED_UPDATE)

        self.assertNotEquals(response.status_code, 200)

    def test_cat_create_staff_required(self):
        response = self.client.get(CAT_CREATE)

        self.assertNotEquals(response.status_code, 200)

    def test_cat_update_staff_required(self):
        response = self.client.get(CAT_UPDATE)

        self.assertNotEquals(response.status_code, 200)

    def test_dog_create_staff_required(self):
        response = self.client.get(DOG_CREATE)

        self.assertNotEquals(response.status_code, 200)

    def test_dog_update_staff_required(self):
        response = self.client.get(DOG_UPDATE)

        self.assertNotEquals(response.status_code, 200)

    def test_pet_list_staff_required(self):
        response = self.client.get(PET_LIST)

        self.assertNotEquals(response.status_code, 200)

    def test_pet_owner_list_staff_required(self):
        response = self.client.get(PET_OWNER_LIST)

        self.assertNotEquals(response.status_code, 200)

    def test_pet_owner_create_staff_required(self):
        response = self.client.get(PET_OWNER_CREATE)

        self.assertNotEquals(response.status_code, 200)
