from django.shortcuts import render
from django.views import generic

from shelter.models import Pet


def index(request):
    num_shelter_cats = Pet.objects.filter(type__name="Cat", left_at=None).count()
    num_shelter_dogs = Pet.objects.filter(type__name="Dog", left_at__isnull=True).count()
    num_home_dogs = Pet.objects.filter(type__name="Dog", left_at__isnull=False).count()
    num_home_cats = Pet.objects.filter(type__name="Cat", left_at__isnull=False).count()

    context = {
        "num_shelter_cats": num_shelter_cats,
        "num_shelter_dogs": num_shelter_dogs,
        "num_home_dogs": num_home_dogs,
        "num_home_cats": num_home_cats
    }
    return render(request, "shelter/index.html", context=context)


class CatListView(generic.ListView):
    model = Pet
    template_name = "shelter/cat_list.html"
    context_object_name = "cat_list"
    queryset = Pet.objects.filter(type__name="Cat").order_by("-arrived_at")
    paginate_by = 5


class DogListView(generic.ListView):
    model = Pet
    template_name = "shelter/dog_list.html"
    context_object_name = "dog_list"
    queryset = Pet.objects.filter(type__name="Dog").order_by("-arrived_at")
    paginate_by = 5


class PetDetailView(generic.DetailView):
    model = Pet
    template_name = "shelter/pet_detail.html"
    context_object_name = "pet_detail"
    queryset = Pet.objects.select_related("type", "breed", "pet_owner")
