from django.db import models

from .dates import week_range
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='menus')
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    

    def __str__(self):
        return self.name


class MealQuerySet(models.QuerySet):
    def week_of(self, date):
        return self.filter(date__range=week_range(date))


class Meal(models.Model):
    menu = models.ForeignKey(
        Menu,
        related_name='meals',
        on_delete=models.CASCADE,
    )
    date = models.DateField(db_index=True)
    type = models.CharField(
        choices=[
            ('lunch', 'Lunch'),
            ('dinner', 'Dinner'),
        ],
        max_length=10,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )
    objects = MealQuerySet.as_manager()

    class Meta:
        unique_together = ['menu', 'date', 'type']
        ordering = ['date', '-type']


class MealItem(models.Model):
    meal = models.ForeignKey(
        Meal,
        related_name='items',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    type = models.CharField(
        choices=[
            ('entre', 'Entre'),
            ('side', 'Side'),
            ('other', 'Other'),
        ],
        max_length=10,
    )
    is_dairy_free = models.BooleanField(
        default=False,
        verbose_name='D',
        help_text='Dairy Free',
    )
    is_gluten_free = models.BooleanField(
        default=False,
        verbose_name='G',
        help_text='Gluten Free',
    )
    is_vegetarian = models.BooleanField(
        default=False,
        verbose_name='V',
        help_text='Vegetarian',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )
    url = models.URLField(max_length=200, default="", blank=True)


class ClientHouse(models.Model):
    name = models.CharField(max_length=100 )
    house_menu = models.ForeignKey(Menu, related_name='menu', on_delete=models.CASCADE)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    

        
