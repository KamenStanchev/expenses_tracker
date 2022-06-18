from django.http import HttpResponse
from django.shortcuts import render

from expenses_tracker.tracker_app.models import Profile


def home_page(request):
    profiles = Profile.objects.all()
    if profiles:
        return render(request, 'home-with-profile.html')
    return render(request, 'home-no-profile.html')


def create_expense(request):
    return render(request, 'expense-create.html')


def edit_expense(request):
    return render(request, 'expense-edit.html')


def delete_expense(request):
    return render(request, 'expense-delete.html')


def profile_page(request):
    return render(request, 'profile.html')


def profile_edit(request):
    return render(request, 'profile-edit.html')


def profile_delete(request):
    return render(request, 'profile-delete.html')
