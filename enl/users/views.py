from django.views.generic import ListView
from .models import MyUser

class MyUserListView(ListView):
    model = MyUser
    ordering = 'id'
    paginate_by = 10
    context_object_name = 'users'
