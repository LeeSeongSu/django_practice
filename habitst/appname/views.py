from django.shortcuts import render, redirect,get_object_or_404
from .models import Post,CustomUser, Hashtag

from .forms import PostForm,SigninForm,UserForm,CommentForm, HashtagForm

# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User

from shop.models import Order

from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from django.contrib import messages

# Create your views here.
def main(request):
    posts = Post.objects.all().order_by('-id')
    users = CustomUser.objects.all()
    signin_form = SigninForm()
    comment_form = CommentForm()
    return render(request, 'appname/main.html', {'posts': posts,'comment_form': comment_form,'users':users,'signin_form':signin_form})
    
def create(request):
    if not request.user.is_active:
        signin_form = SigninForm()
        return render(request, 'appname/signin.html', {'signin_form': signin_form})


    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            
            hashtag_field = form.cleaned_data['hashtag_field']
            str_hashtags = hashtag_field.split('#')
            list_hashtags = list()    

            for hashtag in str_hashtags:
                if Hashtag.objects.filter(name=hashtag):
                    list_hashtags.append(Hashtag.objects.get(name=hashtag))
                else:
                    temp_hashtag = HashtagForm().save(commit=False)
                    temp_hashtag.name = hashtag
                    temp_hashtag.save()
                    list_hashtags.append(temp_hashtag)
                
            post.save()
            post.hashtags.add(*list_hashtags)

            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'appname/create.html', {'form': form})

def read(request):
    return redirect('main')

def update(request, pk):   
    if not request.user.is_active:
        signin_form = SigninForm()
        return render(request, 'appname/signin.html', {'signin_form': signin_form})
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post)
        return render(request,'appname/create.html',{'form':form})
    

def delete(request, pk):
    if not request.user.is_active:
        signin_form = SigninForm()
        return render(request, 'appname/signin.html', {'signin_form': signin_form})
    post = get_object_or_404(Post,pk=pk)
    post.delete()
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
    else:
        signin_form = SigninForm()
        return render(request, 'appname/signin.html', {'signin_form': signin_form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password'],
            nickname = form.cleaned_data['nickname'],
            phone_number = form.cleaned_data['phone_number'],
            profile_image = form.cleaned_data['profile_image'])
            login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('main')
    else:
        form = UserForm()
        return render(request,'appname/signup.html',{'form':form})

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

def hashtag(request,hashtag_name):
    hashtag = get_object_or_404(Hashtag, name=hashtag_name)
    return render(request, 'appname/hashtag.html', {'hashtag': hashtag})

def like(request,pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    post = get_object_or_404(Post,pk=pk)
    user = request.user

    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return redirect('main')

   
    
def profile(request,user_id):
    
    if not request.user.is_active:
        signin_form = SigninForm()
        return render(request, 'appname/signin.html', {'signin_form': signin_form})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            return HttpResponse("로그인 실패. 다시 시도해보세요")
    else:
        posts = Post.objects.all()
        comment_form = CommentForm()
        return render(request, 'appname/profile.html', {'posts': posts,'comment_form': comment_form})
    
    
@login_required 
def profile_update(request):
    if request.method == 'GET':
        return render(request, 'appname/profile_update.html')

    elif request.method == 'POST':
        user = request.user
        email = request.POST.get('email')
        username = request.POST.get('username')
        new_user_pw = request.POST.get('new_user_pw')
        nickname = request.POST.get('nickname')

      
        user.email = email
        user.username = username
        user.nickname = nickname
        user.set_password(new_user_pw)

        user.save()


        return redirect('main')

def search(request):
    posts = Post.objects.all().order_by('-id')
    users = CustomUser.objects.all()
    q = request.POST.get('q', "") 

    if q:
        posts = posts.filter(writer__username__icontains=q)
        return render(request, 'appname/search.html', {'posts' : posts, 'q' : q, 'users' : users})
    
    else:
        return render(request, 'appname/search.html')

def category(request):
    return render(request, 'appname/category.html')

def habittest(request):
    return render(request, 'appname/habittest.html')

def myblog(request):
    return render(request, 'appname/myblog.html')

def mygroup(request):
    return render(request, 'appname/mygroup.html')

# def mypage(request):
#     return render(request, 'appname/mypage.html')

def review(request):
    return render(request, 'appname/review.html')

#def search(request):
    #return render(request, 'appname/search.html')

def withme(request):
    return render(request, 'appname/withme.html')

@login_required
def mypage(request):
    order_list = Order.objects.filter(user=request.user)
    return render(request, 'appname/mypage.html', {
        'order_list': order_list,
    })

@method_decorator(login_required, name='dispatch')
class OrderCancel(RedirectView):
    url = 'mypage'

    def get(self, request, *args, **kwargs):
        queryset = Order.objects.get(imp_uid=self.kwargs.get('imp_uid'))
        try:

            if queryset.status == "cancelled":
                print("여기?")
                messages.error(self.request, '이미 주문을 취소하셨습니다.')
                print("취소가 이미됨")
                return redirect(self.url)

            elif queryset.status == "paid":
                messages.error(self.request, '거래가 완료된 상태입니다.')
                queryset.cancel()
                queryset.update()
                messages.info(self.request, '주문을 취소하셨습니다.')
                print("주문취소?")
                return redirect(self.url)

            queryset.cancel()
            messages.info(self.request, '주문을 취소하셨습니다.')
        except:
            messages.error(self.request, '유효하지 않은 상품입니다.')
            

        return redirect(self.url)
