from django.urls import path, include

from shelter.views import (
    index,
    CatListView,
    DogListView,
    PetDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dogs/",
        DogListView.as_view(),
        name="dog-list"
    ),
    path(
        "cats/",
        CatListView.as_view(),
        name="cat-list"
    ),
    path(
        "pets/<int:pk>/detail/",
        PetDetailView.as_view(),
        name="pet-detail"
    ),
]

app_name = "shelter"
