from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import Post, Reply, User
from .forms import PostForm, ReplyForm, UserForm, CustomUserCreationForm

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    return render(request, 'base/login_register.html', {'page': page})

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(
        Q(content__icontains=q)
    )
    # posts = Post.objects.all()
    replies = Reply.objects.all()
    context = {'posts': posts, 'replies': replies, 'q': q}
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        content = request.POST.get('content')
        Post.objects.create(
            user=request.user,
            content=content
        )
        return redirect('home')
    return render(request, 'base/post_form.html', {'form': form})

def post(request, pk):
    post = Post.objects.get(id=pk)
    replies = post.reply_set.all()

    # create reply
    # replyForm = ReplyForm()
    if request.method == 'POST':
        if 'reply' in request.POST:
            body = request.POST.get('body')
            Reply.objects.create(
                user=request.user,
                post=post,
                body=body
            )
            return redirect('post', pk=post.id)

    context= {'post': post, 'replies': replies}
    return render(request, 'base/post.html', context)

@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.user:
        return HttpResponse('You are not allowed here')
    if request.method == 'POST':
        post.delete()
        return redirect('home')

@login_required(login_url='login')
def updatePost(request, pk):
    page = 'edit'
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.user != post.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post', pk)

    context = {'form': form, 'page': page, 'post': post}
    return render(request, 'base/post_form.html', context)
