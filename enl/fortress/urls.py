from django.urls import path

from . import views

app_name = 'fortress'

urlpatterns = [
    path('', views.FortressListView.as_view(), name='fortress_view'),
]