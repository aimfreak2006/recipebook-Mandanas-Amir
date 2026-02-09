from django.shortcuts import render
from django.http import HttpResponse

recipes = [
    {
        "name": "Recipe 1",
        "link": "recipe/1"
    },
    {
        "name": "Recipe 2",
        "link": "recipe/2"
    }
]

ingredients_1 = [
    {
        "name": "tomato",
        "quantity": "3pcs"
    },
    {
        "name": "onion",
        "quantity": "1pc"
    },
    {
        "name": "pork",
        "quantity": "1kg"
    },
    {
        "name": "water",
        "quantity": "1L"
    },
    {
        "name": "sinigang mix",
        "quantity": "1 packet"
    }
]

ingredients_2 = [
    {
        "name": "garlic",
        "quantity": "1 head"
    },
    {
        "name": "onion",
        "quantity": "1pc"
    },
    {
        "name": "vinegar",
        "quantity": "1/2cup"
    },
    {
        "name": "water",
        "quanity": "1 cup"
    },
    {
        "name": "salt",
        "quantity": "1 tablespoon"
    },
    {
        "name": "whole black peppers",
        "quantity": "1 tablespoon"
    },
    {
        "name": "pork",
        "quantity": "1 kilo"
    }
]

def recipe_list(request):
    dictionary = {"recipes" : recipes}
    return render(request, "ledger/recipe_list.html", dictionary)

def first_recipe(request):
    dictionary = {"ingredients" : ingredients_1}
    return render(request, "ledger/first_recipe.html", dictionary)

def second_recipe(request):
    dictionary = {"ingredients" : ingredients_2}
    return render(request, "ledger/second_recipe.html", dictionary)
