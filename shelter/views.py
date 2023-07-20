from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from shelter.forms import CatForm, DogForm, PetOwnerCreationForm
from shelter.models import Pet, PetOwner


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


class StaffUserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            if self.raise_exception:
                raise PermissionDenied
            else:
                return redirect(reverse("shelter:index"))

        return super(StaffUserRequiredMixin, self).dispatch(request, *args, **kwargs)


class CatListView(generic.ListView):
    model = Pet
    template_name = "shelter/cat_list.html"
    context_object_name = "cat_list"
    queryset = Pet.objects.filter(type__name="Cat").order_by("-arrived_at")
    paginate_by = 5


class CatCreateView(StaffUserRequiredMixin, generic.CreateView):
    form_class = CatForm
    template_name = "shelter/cat_form.html"
    success_url = reverse_lazy("shelter:cat-list")


class CatUpdateView(StaffUserRequiredMixin, generic.UpdateView):
    model = Pet
    form_class = CatForm
    template_name = "shelter/cat_form.html"
    success_url = reverse_lazy("shelter:cat-list")


class DogListView(generic.ListView):
    model = Pet
    template_name = "shelter/dog_list.html"
    context_object_name = "dog_list"
    queryset = Pet.objects.filter(type__name="Dog").order_by("-arrived_at")
    paginate_by = 5


class DogCreateView(StaffUserRequiredMixin, generic.CreateView):
    form_class = DogForm
    template_name = "shelter/dog_form.html"
    success_url = reverse_lazy("shelter:dog-list")


class DogUpdateView(StaffUserRequiredMixin, generic.UpdateView):
    model = Pet
    form_class = DogForm
    template_name = "shelter/dog_form.html"
    success_url = reverse_lazy("shelter:dog-list")


class PetDetailView(generic.DetailView):
    model = Pet
    template_name = "shelter/pet_detail.html"
    context_object_name = "pet_detail"
    queryset = Pet.objects.select_related("type", "breed", "pet_owner")


class PetListView(StaffUserRequiredMixin, generic.ListView):
    model = Pet
    queryset = Pet.objects.select_related("type", "breed", "pet_owner").order_by("-arrived_at")
    paginate_by = 5


class PetOwnerListView(StaffUserRequiredMixin, generic.ListView):
    model = PetOwner
    template_name = "shelter/pet_owner_list.html"
    context_object_name = "pet_owner_list"
    queryset = PetOwner.objects.order_by("-date_joined")
    paginate_by = 5


class PetOwnerCreateView(StaffUserRequiredMixin, generic.CreateView):
    form_class = PetOwnerCreationForm
    template_name = "shelter/pet_owner_form.html"
    success_url = reverse_lazy("shelter:pet-list")


