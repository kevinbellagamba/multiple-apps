from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("Placeholder to display all the surveys created")
def new(request):
    return HttpResponse("Placeholder for users to add a new survey")
