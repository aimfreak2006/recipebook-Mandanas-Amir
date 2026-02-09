from django.urls import path
from .views import recipe_list, first_recipe, second_recipe

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('recipe/1', first_recipe, name='first_recipe'),
    path('recipe/2', second_recipe, name='second_recipe'),
] 

app_name = 'ledger'