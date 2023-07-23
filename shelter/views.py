from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import AccessMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from shelter.forms import (
    BreedSearchForm,
    CatForm,
    DogForm,
    PetOwnerCreationForm,
    PetOwnerUpdateForm,
    CatSearchForm,
    DogSearchForm,
    PetSearchForm,
    PetOwnerSearchForm,
)
from shelter.models import Breed, Pet, PetOwner, Type


def index(request):
    Type.objects.get_or_create(name="Dog")
    Type.objects.get_or_create(name="Cat")

    num_shelter_cats = Pet.objects.filter(
        type__name="Cat", left_at=None
    ).count()
    num_shelter_dogs = Pet.objects.filter(
        type__name="Dog", left_at__isnull=True
    ).count()
    num_home_dogs = Pet.objects.filter(
        type__name="Dog", left_at__isnull=False
    ).count()
    num_home_cats = Pet.objects.filter(
        type__name="Cat", left_at__isnull=False
    ).count()

    context = {
        "num_shelter_cats": num_shelter_cats,
        "num_shelter_dogs": num_shelter_dogs,
        "num_home_dogs": num_home_dogs,
        "num_home_cats": num_home_cats
    }
    return render(request, "shelter/index.html", context=context)


@staff_member_required
def adopt_pet_to_user(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    username = request.POST.get("username")
    pet_owner = get_user_model().objects.get(username=username)

    if pet in pet_owner.pets.all():
        pet.left_at = None
        pet.save()
        pet_owner.pets.remove(pet)
    else:
        pet.left_at = date.today()
        pet.save()
        pet_owner.pets.add(pet)
    pet_owner.save()

    return redirect('shelter:pet-detail', pk=pet.id)


class StaffUserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            if self.raise_exception:
                raise PermissionDenied
            else:
                return redirect(reverse("shelter:index"))

        return super(StaffUserRequiredMixin, self).dispatch(
            request, *args, **kwargs
        )


class RightUserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != kwargs["pk"] and  not request.user.is_staff:
            if self.raise_exception:
                raise PermissionDenied
            else:
                return redirect(reverse("shelter:index"))

        return super(RightUserRequiredMixin, self).dispatch(
            request, *args, **kwargs
        )


class BreedListView(generic.ListView):
    model = Breed
    context_object_name = "breed_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BreedListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        type_ = self.request.GET.get("type", "")

        if name:
            context["search_form"] = BreedSearchForm(initial={
                "name": name,
            })
        if type_:
            context["search_form"] = BreedSearchForm(initial={
                "type": type_,
            })

        return context

    def get_queryset(self):
        name = BreedSearchForm(self.request.GET)
        type_ = BreedSearchForm(self.request.GET)
        queryset = Breed.objects.select_related("type")

        name.is_valid()
        type_.is_valid()

        if name.cleaned_data["name"]:
            return queryset.filter(
                name__icontains=name.cleaned_data["name"]
            )
        elif type_.cleaned_data["type"]:
            return queryset.filter(
                type__name__icontains=name.cleaned_data["type"]
            )

        return queryset


class BreedCreateView(StaffUserRequiredMixin, generic.CreateView):
    model = Breed
    fields = "__all__"
    template_name = "shelter/breed_form.html"
    success_url = reverse_lazy("shelter:breed-list")


class BreedUpdateView(StaffUserRequiredMixin, generic.UpdateView):
    model = Breed
    fields = "__all__"
    template_name = "shelter/breed_form.html"
    success_url = reverse_lazy("shelter:breed-list")


class CatListView(generic.ListView):
    model = Pet
    template_name = "shelter/cat_list.html"
    context_object_name = "cat_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        breed = self.request.GET.get("breed", "")

        if name:
            context["search_form"] = CatSearchForm(initial={
                "name": name,
            })
        elif breed:
            context["search_form"] = CatSearchForm(initial={
                "breed": breed,
            })

        return context

    def get_queryset(self):
        name = CatSearchForm(self.request.GET)
        breed = CatSearchForm(self.request.GET)
        queryset = Pet.objects.filter(
            type__name="Cat", left_at__isnull=True
        ).order_by("arrived_at")

        name.is_valid()
        breed.is_valid()

        if name.cleaned_data["name"]:
            return queryset.filter(
                name__icontains=name.cleaned_data["name"]
            )
        elif breed.cleaned_data["breed"]:
            return queryset.filter(
                breed__name__icontains=breed.cleaned_data["breed"]
            )

        return queryset


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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DogListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        breed = self.request.GET.get("breed", "")

        if name:
            context["search_form"] = CatSearchForm(initial={
                "name": name,
            })
        elif breed:
            context["search_form"] = CatSearchForm(initial={
                "breed": breed,
            })

        return context

    def get_queryset(self):
        name = DogSearchForm(self.request.GET)
        breed = DogSearchForm(self.request.GET)
        queryset = Pet.objects.filter(
            type__name="Dog", left_at__isnull=True
        ).order_by("arrived_at")

        name.is_valid()
        breed.is_valid()

        if name.cleaned_data["name"]:
            return queryset.filter(
                name__icontains=name.cleaned_data["name"]
            )
        elif breed.cleaned_data["breed"]:
            return queryset.filter(
                breed__name__icontains=breed.cleaned_data["breed"]
            )

        return queryset


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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PetListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        breed = self.request.GET.get("breed", "")

        if name:
            context["search_form"] = PetSearchForm(initial={
                "name": name,
            })
        elif breed:
            context["search_form"] = PetSearchForm(initial={
                "breed": breed,
            })

        return context

    def get_queryset(self):
        name = PetSearchForm(self.request.GET)
        breed = PetSearchForm(self.request.GET)
        queryset = Pet.objects.select_related(
            "type", "breed"
        ).order_by("arrived_at")

        name.is_valid()
        breed.is_valid()

        if name.cleaned_data["name"]:
            return queryset.filter(
                name__icontains=name.cleaned_data["name"]
            )
        elif breed.cleaned_data["breed"]:
            return queryset.filter(
                breed__name__icontains=breed.cleaned_data["breed"]
            )

        return queryset


class PetOwnerListView(StaffUserRequiredMixin, generic.ListView):
    model = PetOwner
    template_name = "shelter/pet_owner_list.html"
    context_object_name = "pet_owner_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PetOwnerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        first_name = self.request.GET.get("first_name", "")
        last_name = self.request.GET.get("last_name", "")

        if username:
            context["search_form"] = PetOwnerSearchForm(initial={
                "username": username,
            })
        elif first_name:
            context["search_form"] = PetOwnerSearchForm(initial={
                "first_name": first_name,
            })
        elif last_name:
            context["search_form"] = PetOwnerSearchForm(initial={
                "last_name": last_name,
            })

        return context

    def get_queryset(self):
        username = PetOwnerSearchForm(self.request.GET)
        first_name = PetOwnerSearchForm(self.request.GET)
        last_name = PetOwnerSearchForm(self.request.GET)
        queryset = PetOwner.objects.order_by("date_joined")

        username.is_valid()
        first_name.is_valid()
        last_name.is_valid()

        if username.cleaned_data["username"]:
            return queryset.filter(
                username__icontains=username.cleaned_data["username"]
            )
        elif first_name.cleaned_data["first_name"]:
            return queryset.filter(
                first_name__icontains=first_name.cleaned_data["first_name"]
            )
        elif last_name.cleaned_data["last_name"]:
            return queryset.filter(
                last_name__icontains=last_name.cleaned_data["last_name"]
            )

        return queryset


class PetOwnerCreateView(StaffUserRequiredMixin, generic.CreateView):
    form_class = PetOwnerCreationForm
    template_name = "shelter/pet_owner_form.html"
    success_url = reverse_lazy("shelter:pet-list")


class PetOwnerDetailView(RightUserRequiredMixin, generic.DetailView):
    model = PetOwner
    template_name = "shelter/pet_owner_detail.html"
    context_object_name = "pet_owner_detail"


class PetOwnerUpdateView(RightUserRequiredMixin, generic.UpdateView):
    model = PetOwner
    form_class = PetOwnerUpdateForm
    template_name = "shelter/pet_owner_form.html"
    success_url = reverse_lazy("shelter:index")
