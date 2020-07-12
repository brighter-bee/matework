from rest_framework.generics import ListAPIView
from profiles.serializers import PersonSerializer
from profiles.models import Person
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination


class PersonsPagination(LimitOffsetPagination):
    default_limit = 4
    max_limit = 8


class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('location',)
    search_fields = ('name',)
    pagination_class = PersonsPagination

    # def get_queryset(self):
    #     location = self.request.query_params.get('location', None)
    #     if location is None:
    #         return super().get_queryset()
    #     queryset = Person.objects.all()
    #

