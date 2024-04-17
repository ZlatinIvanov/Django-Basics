from django.urls import path, include

from reexam.recipes.views import catalogue, CreateRecipeView, DetailsRecipeView, DeleteRecipeView, EditRecipeView

urlpatterns = [
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', CreateRecipeView.as_view(), name='create_recipe'),
    path('<int:pk>/',
         include([
             path('details/', DetailsRecipeView.as_view(), name='details_recipe'),
             path('delete/', DeleteRecipeView.as_view(), name='delete_recipe'),
             path('edit/', EditRecipeView.as_view(), name='edit_recipe'),
         ])
    ),
]
