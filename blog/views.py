from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    args = dict()
    posts = []

    for post in Post.objects.all():
        arg = dict()
        arg['title'] = post.title
        arg['content'] = post.content
        posts.append(arg)

    args['posts'] = posts
    return render(request, 'blog/index.html', args)

def examples(request):
    args = dict()
    return render(request, 'blog/examples.html', args)

def page(request):
    args = dict()
    return render(request, 'blog/page.html', args)

def another_page(request):
    args = dict()
    return render(request, 'blog/another_page.html', args)

def contact(request):
    args = dict()
    return render(request, 'blog/contact.php', args)
