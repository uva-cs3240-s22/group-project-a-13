from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Recipe
from .forms import RecipeForm

def index(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        recipe_form = RecipeForm()

    return render(request, 'recipes/recipeLayout.html', {
            'recipe_form': recipe_form})

def detail(request, question_id):
    try:
        recipe = Recipe.objects.get(pk=question_id)
    except Recipe.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'recipes/detail.html', {'recipe': recipe})
    #return HttpResponse("You're looking at recipe %s." %question_id)

def result(request):
    return HttpResponse("Congratulations, your recipe has been submitted!")