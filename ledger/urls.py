from django.urls import path
from .views import recipe_list, first_recipe, second_recipe

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>', first_recipe, name='recipe_detail'),
    path('recipe/<int:pk>', second_recipe, name='second_recipe'),
] 

app_name = 'ledger'