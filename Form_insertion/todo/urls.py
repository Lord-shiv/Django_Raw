from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.todo_form),
    path('list/', views.todo_list)
]
