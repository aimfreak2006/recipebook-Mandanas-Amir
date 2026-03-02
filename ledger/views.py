from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    dictionary = {"recipes" : recipes}
    return render(request, "ledger/recipe_list.html", dictionary)


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    dictionary = {"recipe" : recipe}
    return render(request, "ledger/recipes.html", dictionary)

