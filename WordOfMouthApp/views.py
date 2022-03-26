from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
    # return HttpResponse("Hello, World! This is the start of Group 13's Word of Mouth Project.")
    if request.user.is_authenticated:
        return HttpResponseRedirect('recipes')
    return render(request, 'WordOfMouth/login.html')
