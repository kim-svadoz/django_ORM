from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    text = request.GET.get('text')
    context = {
        'title' : title,
        'text' : text
    }
    return render(request, 'articles/create.html', context)

def introduce(request):
    return render(request, 'articles/introduce.html')