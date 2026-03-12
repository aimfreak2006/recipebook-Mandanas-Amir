from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage
from accounts.models import Profile
from .forms import RecipeForm, RecipeIngredientForm, RecipeImageForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def recipe_list(request):
    recipes = Recipe.objects.all()
    dictionary = {"recipes" : recipes}
    if (request.method == "POST"):
        recipe_form = RecipeForm(request.POST)
        if (recipe_form.is_valid):
            recipe_form.save()
            return redirect('/recipes/list') 
    return render(request, "ledger/recipe_list.html", dictionary)



def recipe_add(request):
    authors = Profile.objects.all()
    recipe_form = RecipeForm()
    dictionary = {
        "authors" : authors, 
        "form" : recipe_form,
    }
    return render(request, "ledger/recipe_add.html", dictionary)

def image_add(request):
    image_form = RecipeImageForm()
    dictionary = {
        "form" : image_form,
    }
    return render(request, "ledger/image_add.html", dictionary)

def recipe_detail(request, pk):
    ingredient_form = RecipeIngredientForm(request.POST)
    image_form = RecipeImageForm(request.POST)

    recipe = Recipe.objects.get(pk=pk)
    ingredients = Ingredient.objects.all()

    dictionary = {
        "recipe" : recipe, 
        "ingredients" : ingredients,
        "form" : ingredient_form,
    }

    if (request.method == "POST"):
        if (ingredient_form.is_valid):
            ingredient_form.save()

        if (image_form.is_valid):
            image_form.save()
    return render(request, "ledger/recipe_detail.html", dictionary)

