# Generated by Django 4.1 on 2023-03-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='recipes',
            field=models.ManyToManyField(to='meal_planner.recipe'),
        ),
    ]