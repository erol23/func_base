from django.urls import path
from .views import home, todoCreate, todoList, todo_List_create, todoDetail, TodoListCreateAPIView,TodoDetailAPIView

urlpatterns = [
    path('', home),
    path('todoList/', todoList),
    path('todoCreate/', todoCreate),
    path('todoListCreate/', todo_List_create),
    path('todoDetail/<int:pk>/', todoDetail),
    path('todoCreateApi/', TodoListCreateAPIView.as_view()),
    path('todoDetailApi/<int:pk>/', TodoDetailAPIView.as_view()),
]
