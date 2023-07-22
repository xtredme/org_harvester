from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    # Если вызван URL без относительного адреса (шаблон — пустые кавычки),
    # то вызывается view-функция index() из файла views.py
    path('', views.HomepageListView.as_view(), name = 'index'),
]