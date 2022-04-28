from tokenize import Token
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RatingSerializer
from rest_framework.authentication import TokenAuthentication
from django.urls import reverse
from .models import Rating

# Create your views here.

# Our Rating view.
class RatingView(viewsets.ModelViewSet):
  # Create a new RatingSerializer instance.
  serializer_class = RatingSerializer
  # Rating.objects.all() retrieves all the Rating objects in the database.
  queryset = Rating.objects.all()
