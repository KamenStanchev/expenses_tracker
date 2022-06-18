from django.http import HttpResponse
from django.shortcuts import render

from expenses_tracker.tracker_app.models import Profile


def home_page(request):
    profiles = Profile.objects.all()
    context ={
        'profiles': profiles,
    }
    return render(request, 'home.html', context)


def create_expense(request):
    pass


def edit_expense(request):
    pass


def delete_expense(request):
    pass


def profile_page(request):
    pass


def profile_edit(request):
    pass


def profile_delete(request):
    pass
