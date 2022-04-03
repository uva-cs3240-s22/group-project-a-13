# Generated by Django 4.0.2 on 2022-04-03 21:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0006_recipe_num_instructions_recipeinstruction'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
