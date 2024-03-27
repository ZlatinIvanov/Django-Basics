from django.views import generic as views
from django.shortcuts import render


class CreateAlbumView(views.CreateView):
    pass


class DetailAlbumView(views.DetailView):
    pass


class EditAlbumView(views.UpdateView):
    pass


class DeleteAlbumView(views.DeleteView):
    pass