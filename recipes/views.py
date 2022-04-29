from multiprocessing import context
from reprlib import recursive_repr
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Recipe, RecipeInstruction, RecipeEquipment, RecipeIngredient
from .forms import RecipeForm
from django.views.generic import TemplateView, ListView
import boto3
from django.db.models import Q # new
from django.contrib.auth import logout
#from .filters import RecipeFilter

def homepage(request):
    recipelist = Recipe.objects.all()
    time_query = request.GET.get('recipe_time')
    type_query = request.GET.get('recipe_type')
    diet_query = request.GET.get('recipe_diet')

    if time_query != '' and time_query is not None:
        recipelist = recipelist.filter(recipe_time=time_query)
    if type_query != '' and type_query is not None:
        recipelist = recipelist.filter(recipe_type=type_query)
    if diet_query != '' and diet_query is not None:
        recipelist = recipelist.filter(recipe_diet=diet_query)

    context = {'recipelist':recipelist}

    
    return render(request, 'recipes/homepage.html', context)

def index(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        recipe_form = RecipeForm()

    return render(request, 'recipes/recipeLayout.html', {
            'recipe_form': recipe_form})

def logout_user(request):
    logout(request)    
    return HttpResponseRedirect(reverse('homepage'))

# def search(request):
#     if request.method == 'POST':
#         recipe = Recipe.objects.get(recipe_name = request.POST)
#         return render(request, 'recipes/search.html', {'recipe': recipe})

class SearchResultsView(generic.ListView):
    model = Recipe
    template_name = 'recipes/search.html'
    context_object_name = 'recipelist'

    def get_queryset(self):  # new
        query = self.request.GET.get("search", None)
        if query:
            object_list = Recipe.objects.filter(
                Q(recipe_name__icontains=query) |
                Q(recipe_description__icontains=query) |
                Q(recipe_ingredients__icontains=query) |
                Q(recipe_equipment__icontains=query) |
                Q(recipe_instructions__icontains=query) |
                Q(user_name__icontains=query)
            )
            return object_list

    # queryset = Recipe.objects.filter(recipe_name__icontains='pizza') # new

def login(request):
    return render(request, 'login.html')

def detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    is_favorited = False
    if recipe.favorites.filter(id=request.user.id).exists():
        is_favorited = True
    context = {
        'recipe': recipe,
        'is_favorited': is_favorited
    }
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipes/detail.html', context)

def result(request):
    return render(request, 'recipes/success.html')

def short(request):
    recipelist = [r for r in Recipe.objects.all() if r.is_short()]
    context = {'recipelist': recipelist}
    return render(request, 'recipes/shortRecipes.html', context)

def long(request):
    recipelist = [r for r in Recipe.objects.all() if not r.is_short()]
    context = {'recipelist': recipelist}
    return render(request, 'recipes/longRecipes.html', context)

def fork(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            '''''
            if not recipe_form.data('recipe_image'):
                new_recipe = recipe_form.save(commit=False)
                new_recipe.recipe_image = recipe.recipe_image
                new_recipe.save()
            else:
            '''
            recipe_form.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        recipe_form = RecipeForm()

    return render(request, 'recipes/forkRecipe.html', {'recipe': recipe})

def add(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
        text = request.POST['instruction']
        recipe.recipeinstruction_set.create(instruction_text = text)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return HttpResponseRedirect(reverse('detail', kwargs = {'recipe_id': recipe_id}))

def add_e(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
        text = request.POST['equipment']
        recipe.recipeequipment_set.create(equipment_text = text)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return HttpResponseRedirect(reverse('detail', kwargs = {'recipe_id': recipe_id}))

def add_i(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
        text = request.POST['ingredient']
        q = request.POST['quantity']
        recipe.recipeingredient_set.create(ingredient_text = text, ingredient_quantity = q)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return HttpResponseRedirect(reverse('detail', kwargs = {'recipe_id': recipe_id}))

def add_instruction(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipes/addInstruction.html', {'recipe': recipe})

def add_equipment(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipes/addEquipment.html', {'recipe': recipe})

def add_ingredient(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, 'recipes/addIngredient.html', {'recipe': recipe})

def delete_instruction(request, instruction_id, recipe_id):
    try:
        recipe_instruction = RecipeInstruction.objects.get(pk = instruction_id)
        recipe_instruction.delete()
    except RecipeInstruction.DoesNotExist:
        raise Http404("Something went wrong")
    return HttpResponseRedirect(reverse('detail', kwargs = {'recipe_id': recipe_id}))

def delete_equipment(request, equipment_id, recipe_id):
    try:
        recipe_equipment = RecipeEquipment.objects.get(pk = equipment_id)
        recipe_equipment.delete()
    except RecipeEquipment.DoesNotExist:
        raise Http404("Something went wrong")
    return HttpResponseRedirect(reverse('detail', kwargs = {'recipe_id': recipe_id}))


def delete_ingredient(request, ingredient_id, recipe_id):
    try:
        recipe_ingredient = RecipeIngredient.objects.get(pk = ingredient_id)
        recipe_ingredient.delete()
    except RecipeIngredient.DoesNotExist:
        raise Http404("Something went wrong")
    return HttpResponseRedirect(reverse('detail', kwargs = {'recipe_id': recipe_id}))

def edit_description(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Something went wrong")
    return render(request, 'recipes/editDescription.html', {'recipe': recipe})

def edit_d(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
        new_name = request.POST['name']
        new_description = request.POST['description']
        new_equipment = request.POST['equipment']
        new_ingredient = request.POST['ingredient']
        new_instruction = request.POST['instruction']
        new_time = request.POST['recipe_time']
        new_type = request.POST['recipe_type']
        new_diet = request.POST['recipe_diet']
        recipe.recipe_name = new_name
        recipe.recipe_description = new_description
        recipe.recipe_equipment = new_equipment
        recipe.recipe_ingredients = new_ingredient
        recipe.recipe_instructions = new_instruction
        recipe.recipe_time = new_time
        recipe.recipe_type = new_type
        recipe.recipe_diet = new_diet
        recipe.save()
    except Recipe.DoesNotExist:
        raise Http404("Something went wrong")
    return HttpResponseRedirect(reverse('detail', kwargs = {'recipe_id': recipe_id}))

def edit_image(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk = recipe_id)
        if 'recipe_image' in request.FILES:
            new_image = request.FILES['recipe_image']
            recipe.recipe_image = new_image
            recipe.save()
    except Recipe.DoesNotExist:
        raise Http404("Something went wrong")
    return HttpResponseRedirect(reverse('detail', kwargs = {'recipe_id': recipe_id}))

def edit_recipe(request, recipe_id):
        try:
            recipe = Recipe.objects.get(pk = recipe_id)
            if request.user.username == recipe.user_name:
                return render(request, 'recipes/editRecipe.html', {'recipe': recipe})
            else:
                raise Http404("You are not authorized to edit this recipe id. Try editing one of your own recipes.")
        except Recipe.DoesNotExist:
            raise Http404("You tried to find a recipe that does not exist.")


def myrecipes(request):
    current_user = request.user
    submitted_recipes = Recipe.objects.filter(user_name=current_user)

    time_query = request.GET.get('recipe_time')
    type_query = request.GET.get('recipe_type')
    diet_query = request.GET.get('recipe_diet')

    if time_query != '' and time_query is not None:
          submitted_recipes =   submitted_recipes.filter(recipe_time=time_query)
    if type_query != '' and type_query is not None:
          submitted_recipes =    submitted_recipes.filter(recipe_type=type_query)
    if diet_query != '' and diet_query is not None:
          submitted_recipes =   submitted_recipes.filter(recipe_diet=diet_query)

    context = {'submitted_recipes': submitted_recipes}
    return render(request, 'recipes/myRecipes.html', context)


def favorited_list(request):
    user = request.user
    favorite_recipes = user.favorites.all()
    time_query = request.GET.get('recipe_time')
    type_query = request.GET.get('recipe_type')
    diet_query = request.GET.get('recipe_diet')

    if time_query != '' and time_query is not None:
        favorite_recipes =  favorite_recipes.filter(recipe_time=time_query)
    if type_query != '' and type_query is not None:
        favorite_recipes =  favorite_recipes.filter(recipe_type=type_query)
    if diet_query != '' and diet_query is not None:
        favorite_recipes =  favorite_recipes.filter(recipe_diet=diet_query)

    context = {'favorite_recipes': favorite_recipes}
    return render(request, 'recipes/favoritedRecipes.html',context)

def favorite_recipe(request):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    is_favorited = False
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
        is_favorited = False
    else:
        recipe.favorites.add(request.user)
        is_favorited = True
    return HttpResponseRedirect(recipe.get_absolute_url())

def favorite_recipe_card(request):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    is_favorited = False
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
        is_favorited = False
    else:
        recipe.favorites.add(request.user)
        is_favorited = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))