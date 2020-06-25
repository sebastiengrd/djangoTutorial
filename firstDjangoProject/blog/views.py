from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Person 1',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'February 12, 2005'
    },
    {
        'author': 'Person 2',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'February 13, 2005'
    }
]



# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})