from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {}
    return render(request, 'main/index.html', ctx)

# View for new people
def first_time(request):
    ctx = {"title":"I'm New"}
    return render(request, 'main/first_time.html', ctx)

def plan_visit(request):
    
    ctx = {"title": "Plan a visit"}
    return render(request, 'visitor/new_visit.html', ctx)

# Authorization Views
def signup(request):
    ctx = {}
    return render(request, 'visitor/signup.html', ctx)

def login(request):
    ctx = {}
    return render(request, 'visitor/login.html', ctx)
