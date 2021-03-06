from django.contrib import admin
from django.urls import path, include

from expenses_tracker.tracker_app.views import home_page, create_expense, edit_expense, delete_expense, profile_page, \
    profile_edit, profile_delete

urlpatterns = [

    path('', home_page, name='home_page'),

    path('create/', create_expense, name='create_expense'),
    path('edit/<str:pk>/', edit_expense, name='edit_expense'),
    path('delete/<str:pk>/', delete_expense, name='delete_expense'),

    path('profile/', profile_page, name='profile_page'),
    path('profile/edit/<str:pk>/', profile_edit, name='profile_edit'),
    path('profile/delete/<str:pk>/', profile_delete, name='profile_delete'),
]
