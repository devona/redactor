from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post


def posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = PostForm()
    posts = Post.objects.all().order_by('id')    
    return render(request,'posts.html',{'form':form, 'posts': posts})

def post_edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':

        form = PostForm(post,request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = PostForm(instance=post)
    return render(request,'post_edit.html',{'form':form, 'post': post})