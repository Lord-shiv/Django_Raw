from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


def todo_list(request):
    context = {
        'todo_list': Todo.objects.all()
    }
    return render(request, "todo/todo_list.html", context)


def todo_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = TodoForm()
        else:
            todo = Todo.objects.get(pk=id)
            form = TodoForm(instance=todo)
        return render(request, "todo/todo_form.html", {'form': form})
    else:
        if id == 0:
            form = TodoForm(request.POST)
        else:
            todo = Todo.objects.get(pk=id)
            form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/todo/list')


def todo_delete(request):
    return
