from django.urls import path

from . import views

app_name = 'downloader'
urlpatterns = [
    path('', views.DownloaderListView.as_view(), name='downloader_view'),
]