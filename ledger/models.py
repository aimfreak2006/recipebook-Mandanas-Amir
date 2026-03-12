from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import Profile


# each class is a table in the database
# each attribute is a field in the table
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="recipes",
        null="True",
        blank="True",
        )
    created_on = models.DateTimeField(default=timezone.now())
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[int(self.id)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name="recipes"
        )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name="ingredients"
        )


class RecipeImage(models.Model):
    recipe_image = models.ImageField(upload_to='images/', null=True)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="images",
    )
