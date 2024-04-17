from django import forms

from reexam.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nickname', "first_name", "last_name", "chef", "bio")