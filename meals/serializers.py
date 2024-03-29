from rest_framework import serializers

from .models import Menu, Meal, MealItem, ClientHouse
from django.contrib.auth.models import User
import json

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name']
    


class MealItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealItem
        fields = ['name', 'type', 'is_dairy_free',
                  'is_gluten_free', 'is_vegetarian', 'url', 'id' ]


class MealSerializer(serializers.ModelSerializer):
    items = MealItemSerializer(many=True)
    class Meta:
        model = Meal
        fields = ['id',  'date', 'type', 'items', 'menu', ]
        validators = []
        


    def create(self, validated_data):
        item_data = validated_data.pop('items')
        meal, created= Meal.objects.update_or_create(**validated_data)
        
        for item_data in item_data:
            MealItem.objects.update_or_create(meal=meal, **item_data)
        return meal
    


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientHouse
        fields = ['id', 'name', 'house_menu', 'password']

class UserSerializer(serializers.ModelSerializer):
    user_permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'user_permissions')

    def get_user_permissions(self, obj):
        print(obj)
        return obj.user_permissions.all()
