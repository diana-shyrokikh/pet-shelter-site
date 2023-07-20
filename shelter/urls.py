from django.urls import path, include

from shelter.views import (
    index,
    CatListView,
    DogListView,
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
]

app_name = "shelter"
