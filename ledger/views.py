from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    recipes = Recipe.objects.all()
    dictionary = {"recipes" : recipes}
    if (request.method == "POST"):
        recipe = Recipe()
        recipe.name = request.POST.get("recipe_name")
        recipe.author = request.POST.get("recipe_author")
        recipe.created_on = request.POST.get("recipe_created")
        recipe.updated_on = request.POST.get("recipe_updated")
        recipe.save()
    return render(request, "ledger/recipe_list.html", dictionary)

@login_required
def recipe_add(request):
    if (request.method == "POST"):
        recipe = Recipe()
        recipe.name = request.POST.get("recipe_name")
        recipe.author = request.POST.get("recipe_author")
        recipe.created_on = request.POST.get("recipe_created")
        recipe.updated_on = request.POST.get("recipe_updated")
        recipe.save()

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    dictionary = {"recipe" : recipe}
    return render(request, "ledger/recipe_detail.html", dictionary)

