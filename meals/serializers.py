from rest_framework import serializers

from .models import Menu, Meal, MealItem


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name']


class MealItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealItem
        fields = ['name', 'type', 'is_dairy_free',
                  'is_gluten_free', 'is_vegetarian']


class MealSerializer(serializers.ModelSerializer):
    items = MealItemSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'date', 'type', 'items']
