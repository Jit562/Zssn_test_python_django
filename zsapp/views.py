
from django.shortcuts import render
from .serializers import *
from rest_framework import generics



# Create your views here.

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class SurvivorList(generics.ListCreateAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

class SurvivorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

