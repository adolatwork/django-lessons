from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def userView(request):
    return HttpResponse('<h1>Assalomu, alaykum!</h1>')
