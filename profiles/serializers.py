from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'user', 'skills', 'location')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
