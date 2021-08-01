# Generated by Django 3.1.7 on 2021-04-28 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20210422_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('house_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='meals.menu')),
            ],
            options={
                'unique_together': {('house_name', 'password')},
            },
        ),
    ]
