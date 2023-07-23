from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from shelter.models import Type, Breed


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123456",
            first_name="AdminfirstName",
            last_name="AdminLastName",
            email="admintest@test.com",
            phone_number="3 80 88 888 88 88"
        )
        self.client.force_login(self.admin_user)

        self.pet_owner = get_user_model().objects.create_user(
            username="test",
            password="usertest123456",
            first_name="FirstName",
            last_name="LastName",
            email="test@test.com",
            phone_number="3 80 88 888 88 89"
        )
        self.type = Type.objects.create(
            name="Dog",
        )
        self.breed = Breed.objects.create(
            name="DogTestBreed",
            type=self.type
        )

    def test_pet_owner_additional_info_listed(self):
        url = reverse("admin:shelter_petowner_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.pet_owner.phone_number)
        self.assertContains(response, self.pet_owner.date_joined.date())

    def test_pet_owner_detailed_phone_number_listed(self):
        url = reverse(
            "admin:shelter_petowner_change",
            args=[self.pet_owner.id]
        )
        response = self.client.get(url)
        self.assertContains(response, self.pet_owner.phone_number)

    def test_pet_owner_created_additional_info_listed(self):
        url = reverse("admin:shelter_petowner_add")
        response = self.client.get(url)

        self.assertContains(response, "First name:")
        self.assertContains(response, "Last name:")
        self.assertContains(response, "Email:")
        self.assertContains(response, "Phone number:")
        self.assertContains(response, "Staff status")

    def test_pet_owner_list_filter(self):
        url = reverse(
            "admin:shelter_petowner_changelist",
        )
        response = self.client.get(url)

        self.assertContains(response, "By date joined")
        self.assertContains(response, "By staff status")

    def test_pet_owner_search_last_name(self):
        self.new_pet_owner = get_user_model().objects.create_user(
            username="newtest",
            password="usertest123456",
            first_name="FirstName",
            last_name="NewLast",
            email="test1@test.com",
            phone_number="3 80 88 888 88 99"
        )

        url = reverse(
            "admin:shelter_petowner_changelist",
        ) + "?q=NewLast"
        response = self.client.get(url)

        self.assertNotContains(response, "LastName")

########
    def test_type_name_listed(self):
        url = reverse("admin:shelter_type_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.type.name)

#########

    def test_breed_list_filter_by_type(self):
        url = reverse(
            "admin:shelter_breed_changelist",
        )
        response = self.client.get(url)

        self.assertContains(response, "By date type")

    def test_breed_search_name(self):
        Breed.objects.create(
            name="DogBreedTest",
            type=self.type
        )

        url = reverse(
            "admin:shelter_breed_changelist",
        ) + "?q=DogBreedTest"
        response = self.client.get(url)

        self.assertNotContains(response, "DogTestBreed")


