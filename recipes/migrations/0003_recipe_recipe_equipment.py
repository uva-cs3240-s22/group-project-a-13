# Generated by Django 4.0.2 on 2022-03-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_recipe_ingredients_recipe_recipe_instructions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_equipment',
            field=models.CharField(default='', max_length=500),
        ),
    ]