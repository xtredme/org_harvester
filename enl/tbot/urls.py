from django.urls import path

from . import views

app_name = 'tbot'

urlpatterns = [
    path('', views.TbotListView.as_view(), name = 'tbot_view'),
]