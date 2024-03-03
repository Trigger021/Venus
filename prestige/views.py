from django.shortcuts import render, redirect
from prestige.models import User


# Create your views here.

def register(request):
    if request.method == 'POST':
        user = User(username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password'])

        user.save()
        redirect('index')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username'],
                               password=request.POST['password']).exists():
            used = User.objects.get(username=request.POST['username'],
                                    password=request.POST['password'])
            return render(request, 'index.html', {'user': used})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def agent_single(request):
    return render(request, 'agent-single.html')


def agent_grid(request):
    return render(request, 'agents-grid.html')


def blog_grid(request):
    return render(request, 'blog-grid.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def property_grid(request):
    return render(request, 'property-grid.html')


def property_single(request):
    return render(request, 'property-single.html')
