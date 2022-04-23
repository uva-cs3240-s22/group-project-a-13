from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('recipe_time', 'recipe_type', 'recipe_diet', 'recipe_name', 'recipe_description', 'recipe_ingredients', 'recipe_equipment', 'recipe_instructions', 'recipe_image', 'recipe_reference', 'user_name')
        
