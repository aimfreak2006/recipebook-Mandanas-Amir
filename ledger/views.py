from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient
#instead of using lists inside this views just use database


# ingredients_1 = [
#     {
#         "name": "tomato",
#         "quantity": "3pcs"
#     },
#     {
#         "name": "onion",
#         "quantity": "1pc"
#     },
#     {
#         "name": "pork",
#         "quantity": "1kg"
#     },
#     {
#         "name": "water",
#         "quantity": "1L"
#     },
#     {
#         "name": "sinigang mix",
#         "quantity": "1 packet"
#     }
# ]

# ingredients_2 = [
#     {
#         "name": "garlic",
#         "quantity": "1 head"
#     },
#     {
#         "name": "onion",
#         "quantity": "1pc"
#     },
#     {
#         "name": "vinegar",
#         "quantity": "1/2cup"
#     },
#     {
#         "name": "water",
#         "quanity": "1 cup"
#     },
#     {
#         "name": "salt",
#         "quantity": "1 tablespoon"
#     },
#     {
#         "name": "whole black peppers",
#         "quantity": "1 tablespoon"
#     },
#     {
#         "name": "pork",
#         "quantity": "1 kilo"
#     }
# ]

def recipe_list(request):
    recipes = Recipe.objects.all()
    dictionary = {"recipes" : recipes}
    return render(request, "ledger/recipe_list.html", dictionary)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    dictionary = {"recipies" : recipe}
    return render(request, "ledger/first_recipe.html", dictionary)

