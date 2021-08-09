from django.urls import path
from .views import home, todoCreate, todoList, todo_List_create, todoDetail

urlpatterns = [
    path('', home),
    path('todoList/', todoList),
    path('todoCreate/', todoCreate),
    path('todoListCreate/', todo_List_create),
    path('todoDetail/<int:pk>/', todoDetail),
]
