from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #dictionary for {{boldmessage}} template
    context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # dictionary for {{boldmessage}} template
    context_dict = {'boldmessage': "This tutorial has been put together by Alex.", }

    return render(request, 'rango/about.html', context=context_dict)

