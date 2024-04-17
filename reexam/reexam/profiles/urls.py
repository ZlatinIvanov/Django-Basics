from django.urls import path

from reexam.profiles.views import EditProfileView, DeleteProfileView, DetailProfileView

urlpatterns = [
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete_profile'),
    path('details/', DetailProfileView.as_view(), name='details_profile'),
]