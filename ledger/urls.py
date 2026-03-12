from django.urls import path
from .views import recipe_list, recipe_detail, recipe_add, image_add

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe_list'),
    path('recipe/add', recipe_add, name="recipe_add"),
    path('recipe/<int:pk>', recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/add_image', image_add, name='image'),
] 

app_name = 'ledger'