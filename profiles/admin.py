from django.contrib import admin
from .models import Person
from .models import Skill

# Register your models here.


class SkillInline(admin.TabularInline):
    model = Skill


class PersonAdmin(admin.ModelAdmin):
    inlines = [SkillInline]


admin.site.register(Person, PersonAdmin)
admin.site.register(Skill)
