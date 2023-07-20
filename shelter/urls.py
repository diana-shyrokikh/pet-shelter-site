from django.urls import path, include

from shelter.views import (
    index,
)

urlpatterns = [
    path("", index, name="index"),
]

app_name = "shelter"
