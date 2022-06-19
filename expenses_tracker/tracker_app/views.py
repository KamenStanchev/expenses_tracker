from django.http import HttpResponse
from django.shortcuts import render, redirect

from expenses_tracker.tracker_app.forms import ProfileForm
from expenses_tracker.tracker_app.models import Profile, Expense


# it is support function
def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    if profile:
        profile_expenses = Expense.objects.filter(owner_profile=profile.pk)
        sum_expenses_price = sum(e.price for e in profile_expenses)
        left_money = profile.budget - sum_expenses_price
        context = {
            'profile': profile,
            'profile_expenses': profile_expenses,
            'left_money': left_money,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page')
        else:
            form = ProfileForm()
        context = {
            'form': form,
            'not_user': True,
        }
    return render(request, 'home-no-profile.html', context)


def create_expense(request):
    return render(request, 'expense-create.html')


def edit_expense(request, pk):
    return render(request, 'expense-edit.html')


def delete_expense(request, pk):
    return render(request, 'expense-delete.html')


def profile_page(request):
    profile = get_profile()

    return render(request, 'profile.html')


def profile_edit(request):
    return render(request, 'profile-edit.html')


def profile_delete(request):
    return render(request, 'profile-delete.html')
