from django import forms

from reexam.recipes.models import Recipe


class CarForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']