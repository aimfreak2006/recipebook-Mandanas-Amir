from django import forms
from accounts.models import Profile
from .models import Recipe, RecipeIngredient, RecipeImage, Ingredient

class RecipeForm(forms.ModelForm):
    name = forms.CharField(label="Recipe Name", max_length = 100)
    author = forms.ModelChoiceField(
        label="Recipe Author", 
        queryset=Profile.objects.all(),
        )

    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeIngredientForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(
        label="Ingredient", 
        queryset=Ingredient.objects.all()
    )
    quantity = forms.CharField(label="Quantity", max_length = 100)

    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class RecipeImageForm(forms.Form):
    recipe_image = forms.ImageField(label="Submit a Picture")
    description = forms.CharField(lable="Description")

    class Meta:
        model = RecipeImage
        fields = '__all__'
