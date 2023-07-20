from django.urls import path, include

from shelter.views import (
    index,
    CatListView,
    CatCreateView,
    CatUpdateView,
    DogListView,
    DogCreateView,
    DogUpdateView,
    PetDetailView,
    PetListView,
    PetOwnerListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dogs/",
        DogListView.as_view(),
        name="dog-list"
    ),
    path(
        "dogs/create/",
        DogCreateView.as_view(),
        name="dog-create"
    ),
    path(
        "dogs/<int:pk>/update/",
        DogUpdateView.as_view(),
        name="dog-update"
    ),
    path(
        "cats/",
        CatListView.as_view(),
        name="cat-list"
    ),
    path(
        "cats/create/",
        CatCreateView.as_view(),
        name="cat-create"
    ),
    path(
        "cats/<int:pk>/update/",
        CatUpdateView.as_view(),
        name="cat-update"
    ),
    path(
        "pets/<int:pk>/detail/",
        PetDetailView.as_view(),
        name="pet-detail"
    ),
    path(
        "pets/",
        PetListView.as_view(),
        name="pet-list"
    ),
    path(
        "users/",
        PetOwnerListView.as_view(),
        name="pet-owner-list"
    ),
    path("accounts/", include("django.contrib.auth.urls")),
]

app_name = "shelter"
