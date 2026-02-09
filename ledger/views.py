from django.shortcuts import render
from django.http import HttpResponse

recipes = [
    {
        "name": "Recipe 1",
        "ingredients": [
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
        ],
        "link": "recipe/1"
    },
    {
        "name": "Recipe 2",
        "ingredients": [
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
        ],
        "link": "recipe/2"
    }
]

def recipe_list(request):
    dictionary = {"recipes" : recipes}
    return render(request, "ledger/recipe_list.html", dictionary)

def first_recipe(request):
    dictionary = {"ingredients" : recipes[0]['ingredients']}
    return render(request, "ledger/first_recipe.html", dictionary)

def second_recipe(request):
    dictionary = {"ingredients" : recipes[1]['ingredients']}
    return render(request, "ledger/second_recipe.html", dictionary)
