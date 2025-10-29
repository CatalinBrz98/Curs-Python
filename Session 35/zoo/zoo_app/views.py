from django.shortcuts import render, redirect
from .models import Species
from .forms import SpeciesForm


def index(request):
    context = {"message": "Hello, user. Here is the home page for the zoo_app application."}
    return render(request, 'zoo_app/index.html', context)



def species_list(request):
    species = Species.objects.all()

    context = {"species_list": species}
    return render(request, 'zoo_app/species_list.html', context)


def add_species(request):
    if request.method == "POST":
        form = SpeciesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = SpeciesForm()
    return render(request, 'zoo_app/add_species.html', {'form': form})
