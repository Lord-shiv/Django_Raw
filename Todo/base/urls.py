from django.contrib import admin
from django.urls import path
from todo_app.views import todo_home, delete_todo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo-home/", todo_home, name="todo-home"),
    path("delete-todo/<int:todo_id>/", delete_todo, name="delete"),
]
