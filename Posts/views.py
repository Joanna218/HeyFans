# from django.forms.models import modelform_factory
# from .forms import StoreForm
from .models import Posts
from django.shortcuts import render, redirect

from django.http import HttpResponse
# Create your views her


def posts_list(request):
    posts = Posts.objects.all()  # 從資料庫抓資料
    return render(request, 'posts/posts_list.html', {'posts': posts})
    # return HttpResponse('Welcome!~')
