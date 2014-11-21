from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to GameData Api v1.")

def game(request):
    return HttpResponse("Game")

def user(request):
    return HttpResponse("User")
