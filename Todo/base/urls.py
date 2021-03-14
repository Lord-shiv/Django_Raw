from django.contrib import admin
from django.urls import path
from todo_app.views import todo_home, add_todo, delete_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo-home/', todo_home),
    path('add-todo/', add_todo),
    path('delete-todo/<int:todo_id>/', delete_todo),
]
