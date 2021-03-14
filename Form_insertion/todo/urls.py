from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.todo_form, name='todo_form'),  # get post
    path('<int:id>/', views.todo_form, name='todo_update'),
    path('list/', views.todo_list, name='todo_list')
]
