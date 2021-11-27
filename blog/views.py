from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'zulfan',
        'title' : 'blog post 1',
        'content': 'first post content',
        'date' : 'June 12, 2020'
    },
    {
        'author': 'rapli',
        'title' : 'blog post 2',
        'content': 'second post content',
        'date' : 'June 13, 2020'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'about'})

