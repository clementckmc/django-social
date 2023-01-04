from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'base/home.html', context)

def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        # Post.objects.create(
        #     user=request.POST.get('user'),
        #     content=request.POST.get('content')
        # )
        return redirect('home')
    return render(request, 'base/post_form.html', {'form': form})
