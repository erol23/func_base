from django.http.response import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view

from .serializers import TodoSerializer
from .models import Todo

from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, get_object_or_404

from rest_framework import generics

def home(request):
    return HttpResponse('<center><h1 style= "background-color: green">Welcome to todo app</h1></center>')

@api_view(['GET'])
def todoList(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def todo_List_create(request):
    if request.method == 'GET':
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todoDetail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        queryset = Todo.objects.all()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TodoListCreateAPIView(APIView):
    def get(self, request):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class TodoDetailAPIView(APIView):
    def get_object(self, pk):
        todo = get_object_or_404(Todo, pk=pk)
        return todo

    def get(self,request, pk):
        todo = self.get_object(pk= pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk = pk)
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        todo = self.get_object(pk = pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TodoListCreateApi(generics. ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailApi(generics. RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

