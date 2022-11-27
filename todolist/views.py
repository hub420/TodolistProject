#is the logic of the projects take a requests a return a response like html or redirect
from django.shortcuts import render
from .models import Todolist

# Create your views here.

def index(request):
    todo_items = Todolist.objects.order_by('id')
    context = {'todo_items': todo_items}
    return render(request, 'todolist/index.html', context)

