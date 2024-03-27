from django.shortcuts import render, redirect

from ExamPrep.albums.models import Album
from ExamPrep.common.profile_helpers import get_profile
from ExamPrep.web.forms import CreateProfileForm


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form,
        'not_nav': True,
    }

    return render(request, 'web/home-no-profile.html', context)

def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        "albums": Album.objects.all(),
    }
    return render(request, 'web/home-no-profile.html', context)
