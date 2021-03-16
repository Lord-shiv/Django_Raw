from django.shortcuts import render, redirect
from django.contrib import messages

from .models import TodoItem
from .forms import TodoForm

# Create your views here.


def todo_home(request):
    all_items = TodoItem.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Added successfully"))
            return redirect("todo-home")
    form = TodoForm()
    context = {"form": form, "all_items": all_items}
    return render(request, "home.html", context)


def delete_todo(request, todo_id):
    d_item = TodoItem.objects.get(id=todo_id)
    d_item.delete()
    messages.info(request, "removed Successfully!")
    return redirect("todo-home")


def mark_complete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect("todo-home")


def mark_incomplete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect("todo-home")
