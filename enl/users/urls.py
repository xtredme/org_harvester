from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.MyUserListView.as_view(), name='users_view'),
]