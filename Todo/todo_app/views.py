from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.


def todo_home(request):
    all_items = TodoItem.objects.all()
    if request.method == 'POST':
        if "taskAdd" in request.POST:
            author = request.POST["author"]
            content = request.POST['content']
            date = str(request.POST["date"])
            email = request.POST['email']
            phone = request.POST['phone']
            Todo = TodoItem(author=author, content=content,
                            phone=phone, email=email)
    return render(request, 'home.html',
                  {'all_items': all_items})


def add_todo(request):
    # c = request.POST['content']
    # new_item = TodoItem(content = c)
    new_item = TodoItem(
        content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo-home/')


def delete_todo(request, todo_id):
    item_to_delete = TodoItem.objects.get(Sr_no=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo-home/')
