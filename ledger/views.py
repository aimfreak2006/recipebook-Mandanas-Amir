from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage
from accounts.models import Profile
from .forms import RecipeForm, RecipeIngredientForm, RecipeImageForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
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

def image_add(request, pk):
    image_form = RecipeImageForm()
    recipe = Recipe.objects.get(pk=pk)

    dictionary = {
        "recipe" : recipe,
        "form" : image_form,
    }
    return render(request, "ledger/adding_image.html", dictionary)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    dictionary = {
        "recipe" : recipe,
    }
    
    if (request.method == "POST"):
        image_form = RecipeImageForm(request.POST, request.FILES)
        if (image_form.is_valid):
            image_form.save()
        
    return render(request, "ledger/recipe_detail.html", dictionary)

