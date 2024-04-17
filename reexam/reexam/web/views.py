from django.shortcuts import render, redirect

from reexam.common.profile_helpers import get_profile
from reexam.profiles.forms import CreateProfileForm


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    return render(request, 'web/index.html')


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        print("POST request received")
        print("Form data:", request.POST)

    if form.is_valid():
        print("Form is valid")
        form.save()
        return redirect('index')
    else:
        print("Form is not valid")
        print("Errors:", form.errors)

    context = {
        'form': form,
        "no_nav": True,
    }
    return render(request, 'profile/create-profile.html', context)