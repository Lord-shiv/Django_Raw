from django.shortcuts import render
from .forms import TodoForm


def todo_list(request):
    return render(request, "todo/todo_list.html")


def todo_form(request):
    form = TodoForm()
    return render(request, "todo/todo_form.html", {'form': form})


def todo_delete(request):
    return
