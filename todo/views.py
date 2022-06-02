from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .forms import TodoForm

from .models import Todo
# Create your views here.

class Home(TemplateView):
    template_name="todo/home.html"

class TodoCreate(CreateView):
    model= Todo
    form_class = TodoForm
    template_name = "todo/todo_add.html"
    success_url = reverse_lazy("list")

class TodoList(ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    #+ context_object_name = "todos"

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_update.html"
    success_url = reverse_lazy("list")
    # pk_url_kwarg="id"

class TodoDelete(DeleteView):
    model = Todo
    template_name = "todo/todo_delete.html"
    success_url = reverse_lazy("list")

def isCompleted(request,id):
    todo = Todo.objects.get(id=id)
    todo.completed = not(todo.completed)
    todo.save()
    return redirect('list')