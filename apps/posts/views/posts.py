from django.shortcuts import render


def index(request):
    return render(request, 'posts/pages/index.html')


def create(request):
    pass


def update(request):
    pass


def delete(request):
    pass
