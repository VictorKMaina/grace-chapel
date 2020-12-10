from django.shortcuts import Http404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, login, logout

from .models import *
from .form import *
from .email import send_visitor_welcome

User = get_user_model()


def index(request):
    user = request.user
    print(user)

    ctx = {}
    return render(request, 'main/index.html', ctx)

# View for new people


def first_time(request):
    ctx = {"title": "I'm New"}
    return render(request, 'main/first_time.html', ctx)


def plan_visit(request):
    errors = []
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        adults = int(data.get('adults'))
        children = int(data.get('children'))

        if len(first_name) > 0 and len(last_name) > 0 and len(email) > 0:
            new_visitor = Visitor.objects.create(first_name=data.get('first_name'), last_name=data.get('last_name'), email=data.get('email'), adults_count=data.get('adults'), children_count=data.get('children'))

            send_visitor_welcome(request, new_visitor)

            

            return redirect("success/")
        else:
            error = "Invalid info. Please try again."
            ctx = {"title": "Plan a visit", "error": error}
            return render(request, 'visitor/new_visit.html', ctx)

    ctx={"title": "Plan a visit"}
    return render(request, 'visitor/new_visit.html', ctx)

def visit_success(request):
    ctx = {}
    return render(request, "visitor/success.html", ctx)

# Sermon Engine
def sermons(request):
    ctx= {}
    return render(request, "sermon/search_page.html", ctx)


def watch(request):
    ctx = {}
    return render(request, "sermon/video_sermon.html", ctx)

# Authorization Views
def signup(request):
    if request.method == 'POST':
        form = SignupForm(data = request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.filter(username = form.data.get('username')).first()
            user.set_password(form.data.get('password'))
            user.is_active = True
            user.save()
            return redirect('/auth/login/')
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = User.objects.filter(username = form.data.get('username')).first()
            if user is not None or user.check_password(form.data.get('password')):
                login(request, user)
                return redirect('/')

        else:
            error = "Invalid username or password. Please try again."
            ctx = {'form': form, "error":error}
            form = AuthenticationForm()
            return render(request, 'auth/login.html', ctx)

    form = AuthenticationForm()
    ctx = {'form': form}
    return render(request, 'auth/login.html', ctx)

def log_out(request):
    logout(request)
    return redirect('/')
