from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("rango says hi i guess. <a href='/rango/about'> about! </a> ")

def about(request):
    return HttpResponse("rango says this is the abouts page.<a href='/rango/'> index! </a> ")

