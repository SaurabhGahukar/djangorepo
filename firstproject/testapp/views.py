from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse('<h1>Hello Welcome To My first Django Project</h1>')
