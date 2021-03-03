from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("Hello World!")
def second(request):
    return HttpResponse("Welcome to home page!")
def third(request):
    return HttpResponse("Welcome to scaler page!")
def fourth(request, name):
    return HttpResponse("Welcome " + name + "!")
def fifth(request):
    return HttpResponse("<h1> About Me </h1><p> I Love Football </p>")
