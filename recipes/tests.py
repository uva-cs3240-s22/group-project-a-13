from django.test import TestCase

# Create your tests here.
from .models import Recipe

class TestRecipe(TestCase):
    def test_short_recipe(self):
        r = Recipe.objects.create(recipe_name = "1", recipe_ingredients = "1", recipe_instructions = "1")
        self.assertIs(r.is_short(), True)

    def test_long_recipe(self):
        r = Recipe.objects.create(recipe_name = "1", recipe_ingredients = "1", 
        recipe_instructions = "Procedure: Preheat the oven to 325 degrees F (165 degrees C). Grease cookie sheets or line with parchment paper. Sift together the flour, baking soda and salt; set aside. In a medium bowl, cream together the melted butter, brown sugar and white sugar until well blended. Beat in the vanilla, egg, and egg yolk until light and creamy. Mix in the sifted ingredients until just blended. Stir in the chocolate chips by hand using a wooden spoon. Drop cookie dough 1/4 cup at a time onto the prepared cookie sheets. Cookies should be about 3 inches apart. Bake for 15 to 17 minutes in the preheated oven, or until the edges are lightly toasted. Cool on baking sheets for a few minutes before transferring to wire rack.")
        self.assertIs(r.is_short(), False)