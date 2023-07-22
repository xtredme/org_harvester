from django.views.generic import ListView
from users.views import MyUser

class BuildingsListView(ListView):
    model = MyUser
    ordering = 'id'
    paginate_by = 10