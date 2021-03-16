from django.shortcuts import render, redirect
from django.contrib import messages

from .models import TodoItem
from .forms import TodoForm

# Create your views here.


def todo_home(request):
    all_items = TodoItem.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo-home")
    form = TodoForm()
    context = {"form": form, "all_items": all_items, "title": "TODO LIST"}
    return render(request, "home.html", context)


def delete_todo(request, todo_id):
    d_item = TodoItem.objects.get(id=todo_id)
    d_item.delete()
    messages.info(request, "item removed !!!")
    return redirect("todo-home")
