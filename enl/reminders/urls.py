from django.urls import path

from . import views

app_name = 'reminders'

urlpatterns = [
    path('', views.RemindersListView.as_view(), name='reminders_view'),
]