from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.

def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request, id):
    try:
        post= Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def archieves(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'archieves.html',{'post_list':post_list,'error':False})
def test(request):
    return render(request, 'test.html' , {'current_time':datetime.now()})

def blog_search(request):
    if  's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains= s)
            if len(post_list) == 0:
                return render(request,'archieves.html',{'post_list':post_list,'error':True})
            else:
                return render(request,'archieves.html',{'post_list':post_list,'error':False})
        return redirect('/')
