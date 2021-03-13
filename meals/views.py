from django.shortcuts import render
from rest_framework import viewsets

from .models import Meal
from .serializers import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.week_of()
    serializer_class = MealSerializer
