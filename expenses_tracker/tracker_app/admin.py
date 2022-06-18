from django.contrib import admin

# Register your models here.
from expenses_tracker.tracker_app.models import Expense, Profile


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass