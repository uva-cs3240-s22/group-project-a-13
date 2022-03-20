from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def detail(request, question_id):
    return HttpResponse("You're looking at recipe %s." %question_id)