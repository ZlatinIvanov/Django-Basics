from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from reexam.common.profile_helpers import get_profile
from reexam.recipes.models import Recipe


class ReadonlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form


def catalogue(request):

    context = {
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'recipe/catalogue.html', context)


class EditRecipeView(views.UpdateView):
    model = Recipe
    template_name = 'recipe/edit-recipe.html'
    fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
    success_url = reverse_lazy('catalogue')


class DeleteRecipeView(ReadonlyViewMixin, views.DeleteView):
    model = Recipe
    template_name = 'recipe/delete-recipe.html'

    form_class = modelform_factory(
        Recipe,
        fields=('title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url'),
    )
    success_url = reverse_lazy('catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs


class DetailsRecipeView(views.DetailView):
    queryset = Recipe.objects.all()
    template_name = 'recipe/details-recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context['object']
        ingredients_list = recipe.ingredients.split(', ')
        context['ingredients_list'] = ingredients_list
        return context


class CreateRecipeView(views.CreateView):
    model = Recipe
    fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
    template_name = 'recipe/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        profile = get_profile()
        form.instance.author = profile
        return super().form_valid(form)