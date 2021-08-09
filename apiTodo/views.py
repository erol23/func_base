from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<center><h1 style= "background-color: green">Welcome to todo app</h1></center>')
