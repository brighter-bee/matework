from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import Person

# Create your views here.


def index(request):
    return render(request, 'index.html', {'persons': Person.objects.all()})


def person(request, person_id):
    person_ = get_object_or_404(Person, pk=person_id)
    persons = Person.objects.all().exclude(pk=person_id)
    for s in person_.skills.all():
        persons = persons.filter(skills__name__contains=s)
    return render(request, 'profile.html', {'person': person_, 'persons': persons})
