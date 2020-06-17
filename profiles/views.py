from django.shortcuts import render
from .models import Person

# Create your views here.


def index(request):
    return render(request, 'index.html', {'persons': Person.objects.all().order_by('name')[:5]})
