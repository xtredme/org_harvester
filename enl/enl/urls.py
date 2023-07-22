
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace='homepage')),
    path('buildings/', include('buildings.urls', namespace='buildings')),
    path('downloader/', include('downloader.urls', namespace='downloader')),
    path('fortress/', include('fortress.urls', namespace='fortress')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('reminders/', include('reminders.urls', namespace='reminders')),
    path('tbot/', include('tbot.urls', namespace='tbot')),
    path('users/', include('users.urls', namespace='users')),

]
