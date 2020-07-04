from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    location = models.TextField(default="")

    def __str__(self):
        return self.name + " - " + self.user.username

    def username(self):
        return self.user.username
