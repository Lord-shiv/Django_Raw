from django.contrib import admin
from django.urls import path
from todo_app.views import todo_home, delete_todo, mark_complete, mark_incomplete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo-home/", todo_home, name="todo-home"),
    path("delete-todo/<int:todo_id>/", delete_todo, name="delete"),
    path("mark_complete/<int:todo_id>", mark_complete, name="mark_complete"),
    path("mark_incomplete/<int:todo_id>", mark_incomplete, name="mark_incomplete"),
]
