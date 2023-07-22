from django.views.generic import ListView
from users.views import MyUser

class TbotListView(ListView):
    model = MyUser
    ordering = 'id'
    paginate_by = 10
