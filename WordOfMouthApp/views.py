from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    # return HttpResponse("Hello, World! This is the start of Group 13's Word of Mouth Project.")
    return render(request, 'WordOfMouth/index.html')
    
