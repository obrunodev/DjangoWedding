from django.shortcuts import render


def register(request):
    if request.method == 'GET':
        return render(request, 'accounts/pages/register.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'account/pages/login.html')
