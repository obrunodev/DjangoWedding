from django.shortcuts import redirect, render

from ..models import Post
from ..forms import PostForm


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/pages/index.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
        return redirect('posts:create')
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/pages/create.html', context)


def update(request):
    pass


def delete(request):
    pass
