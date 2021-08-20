from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("This is my response!")

def register(request):
    return HttpResponse("Placeholder for users to create a new user record")

def login(request):
    return HttpResponse("Placeholder for users to login")

def users(request):
    return HttpResponse("Placeholder to later display a list of all users")


