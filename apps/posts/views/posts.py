from django.shortcuts import get_object_or_404, redirect, render

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
        return render(request, 'posts/pages/create.html', {
            'form': form
        })
    else:
        form = PostForm()
        return render(request, 'posts/pages/create.html', {
            'form': form
        })


def update(request, pk):
    pass


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:index')
    else:
        context = {'post': post}
        return render(request, 'posts/pages/delete.html', context)
