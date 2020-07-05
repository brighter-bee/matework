from django.shortcuts import render, get_object_or_404
from .models import Person, Skill
from .models import User


# Create your views here.


def index(request):
    return render(request, 'index.html', {'persons': Person.objects.all()})


def person(request, person_id):
    person_ = get_object_or_404(Person, pk=person_id)
    persons = Person.objects.all().exclude(pk=person_id)
    for s in person_.skills.all():
        persons = persons.filter(skills__name__contains=s)
    return render(request, 'profile.html', {'person': person_, 'persons': persons})


def profile(request, request_username):
    if request.method == "POST":
        name = request.POST['name']
        location = request.POST['location']
        skill = request.POST['skill']
        skill_exist = len(Skill.objects.all().filter(name__iexact=skill))
        if not skill_exist:
            skill = Skill(name=skill)
            skill.save()
            print(skill.id)
        else:
            skill = Skill.objects.all().get(name__iexact=skill)
        user_id = get_object_or_404(User, username=request_username)
        Person.objects.filter(user=user_id).update(name=name, location=location)
        Person.objects.get(user=user_id).skills.add(skill.id)
    user_id = get_object_or_404(User, username=request_username)
    person_ = get_object_or_404(Person, user=user_id)
    skills = Skill.objects.all()
    current_username = request.user.username
    allow_edit = current_username == request_username
    return render(request, 'profile.html', {'person': person_, 'allow_edit': allow_edit, 'skills': skills})
