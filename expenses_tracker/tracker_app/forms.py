from django import forms

from expenses_tracker.tracker_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
