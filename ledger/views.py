from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient
from django.contrib.auth.decorators import login_required

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    dictionary = {"recipes" : recipes}
    return render(request, "ledger/recipe_list.html", dictionary)

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    dictionary = {"recipe" : recipe}
    return render(request, "ledger/recipes.html", dictionary)

