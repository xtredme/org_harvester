from django.views.generic import ListView
from users.views import MyUser
from buildings.models import buildhello
class DownloaderListView(ListView):
    model = MyUser
    ordering = 'id'
    paginate_by = 10

buildhello()
