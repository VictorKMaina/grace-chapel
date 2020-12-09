from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {}
    return render(request, 'main/index.html', ctx)