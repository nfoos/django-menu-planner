# Generated by Django 3.1.7 on 2021-12-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_auto_20211201_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='url',
        ),
        migrations.AddField(
            model_name='mealitem',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
