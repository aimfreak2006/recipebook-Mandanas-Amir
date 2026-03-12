from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient
from accounts.models import Profile
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    recipes = Recipe.objects.all()
    dictionary = {"recipes" : recipes}

    if (request.method == "POST"):
        recipe = Recipe()
        recipe.name = request.POST.get("recipe_name")
        author_primary_key = int(request.POST.get("recipe_author"))
        recipe.author = Profile.objects.get(pk=author_primary_key)
        recipe.created_on = request.POST.get("recipe_created")
        recipe.updated_on = request.POST.get("recipe_updated")
        recipe.save()

    return render(request, "ledger/recipe_list.html", dictionary)

def recipe_add(request):
    authors = Profile.objects.all()
    dictionary = {"authors" : authors}
    return render(request, "ledger/recipe_add.html", dictionary)

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = Ingredient.objects.all()
    dictionary = {"recipe" : recipe, "ings" : ingredients}

    if (request.method == "POST"):
        recipe_ingredient = RecipeIngredient()
        recipe_ingredient.recipe = recipe
        ingredient_primary_key = int(request.POST.get("ingredient"))
        recipe_ingredient.ingredient = Ingredient.objects.get(pk=ingredient_primary_key)
        recipe_ingredient.quantity = request.POST.get("quantity")
        recipe_ingredient.save()

    return render(request, "ledger/recipe_detail.html", dictionary)

