from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Recipe(models.Model):
    
    '''''
    TIME_CHOICES= [
    ('5-15', '5 to 15 minutes'),
    ('15-30', '15 to 30 minutes'),
    ('30-60', '30 minutes to an hour'),
    ('60+', 'Over an hour'),
    ]

    TYPE_CHOICES = [
    ('breakfast', "Breakfast"), 
    ('snack', "Snack"), 
    ('lunch', "Lunch"),
    ('dinner', "Dinner"),
    ('dessert', "Dessert"),
    ]

    DIET_CHOICES = [
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'), 
        ('gluten-free', 'Gluten-Free'), 
        ('nut-free', "Nut-Free"),
    ]
    recipe_time = models.CharField(max_length=30, choices=TIME_CHOICES,)
    recipe_type = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True,)
    recipe_diet = models.CharField(max_length=30, choices=DIET_CHOICES, blank=True,)

    '''

    recipe_name = models.CharField(max_length = 50, default = '')
    recipe_description = models.CharField(max_length=1000, default = '')
    recipe_ingredients = models.CharField(max_length = 500, default = '')
    recipe_equipment = models.CharField(max_length = 500, default = '')
    recipe_instructions = models.CharField(max_length = 1000, default = '')
    recipe_image = models.ImageField(default='', upload_to='media/', blank = True)
    recipe_reference = models.IntegerField(default = 0, null = True)
    favorites = models.ManyToManyField(User, related_name="favorites", blank=True)
    user_name = models.CharField(max_length = 50, default = '')
   
    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


    def is_short(self):
        length = len(self.recipe_instructions)
        return length <= 500


class RecipeInstruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    instruction_text = models.CharField(max_length = 500, default = '')

    def __str__(self):
        return self.instruction_text

class RecipeEquipment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    equipment_text = models.CharField(max_length = 100, default = '')

    def __str__(self):
        return self.equipment_text

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_text = models.CharField(max_length = 100, default = '')
    ingredient_quantity = models.CharField(max_length = 100, default = '')

    def __str__(self):
        return self.ingredient_text