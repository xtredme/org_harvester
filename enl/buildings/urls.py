from django.urls import path

from . import views

app_name = 'buildings'

urlpatterns = [
    path('', views.BuildingsListView.as_view(), name='buildings_view'),
]