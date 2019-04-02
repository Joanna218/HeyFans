from .models import Posts
from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'posts/home.html')


def posts_list(request):
    posts = Posts.objects.all()  # 從資料庫抓資料
    return render(request, 'posts/posts_list.html', {'posts': posts})
    # return HttpResponse('Welcome!~')


def posts_detail(request, pk):
    try:
        posts = Posts.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    return render(request, 'posts/posts_detail.html', {'posts': posts})
