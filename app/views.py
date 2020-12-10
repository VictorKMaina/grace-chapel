from django.contrib.auth import get_user_model
from django.shortcuts import Http404, redirect, render

from .models import *

User = get_user_model()


def index(request):
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

# Authorization Views
def signup(request):
    ctx={}
    return render(request, 'visitor/signup.html', ctx)

def login(request):
    ctx={}
    return render(request, 'visitor/login.html', ctx)
