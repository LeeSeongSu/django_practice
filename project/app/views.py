from django.shortcuts import render, redirect,get_object_or_404
from .models import Article,CustomUser
from .forms import ArticleForm,SigninForm,UserForm,CommentForm
import requests
# Create your views here.

from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def main(request):
    posts = Article.objects.all()
    signin_form = SigninForm()
    comment_form = CommentForm()

    return render(request, 'app/main.html', {'posts': posts,'comment_form': comment_form,'signin_form': signin_form})
    
def create(request):
    if not request.user.is_active:
        return HttpResponse("Can't write a post without Sign In")

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.writer = request.user
            form.save()
            return redirect('main')
    else:
        form = ArticleForm()
        return render(request, 'app/create.html', {'form': form})

def read(request):
    return redirect('main')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            return HttpResponse("로그인 실패. 다시 시도해보세요")
            
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password'],
            nickname = form.cleaned_data['nickname'],
            phone_number = form.cleaned_data['phone_number'],
            grade = form.cleaned_data['password'],
            major = form.cleaned_data['nickname'])
            
            login(request, new_user)
            return redirect('main')
    else:
        form = UserForm()
        return render(request,'app/signup.html',{'form':form})

def comment(request,post_id):
    if not request.user.is_active:
        return HttpResponse("Can't write a post without Sign In")
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.c_writer = request.user
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('main')
def detail(request):
    return render(request,'app/detail.html')
