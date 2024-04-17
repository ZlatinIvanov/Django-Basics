from django.urls import reverse_lazy
from django.views import generic as views

from reexam.common.profile_helpers import get_profile
from reexam.recipes.models import Recipe


class DeleteProfileView(views.DeleteView):

    template_name = "profile/delete-profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, quesryset=None):
        return get_profile()


class DetailProfileView(views.DetailView):
    template_name = 'profile/details-profile.html'

    def get_object(self, queryset=None):
        return get_profile()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.object

        total_recipes = Recipe.objects.filter(author=profile).count()

        context['total_recipes'] = total_recipes
        return context


class EditProfileView(views.UpdateView):

    template_name = 'profile/edit-profile.html'
    fields = ('nickname', 'first_name', 'last_name', 'chef', 'bio',)
    success_url = reverse_lazy('details_profile')


    def get_object(self, quesryset=None):
        return get_profile()