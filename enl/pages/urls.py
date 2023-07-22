from django.urls import path

from . import views
app_name = 'pages'

urlpatterns = [
    path('', views.PagesListView.as_view(), name='pages_view'),
]