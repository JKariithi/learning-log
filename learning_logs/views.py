from django.shortcuts import render

# Create your views here.


def index(request):
    """Learning log Home page"""
    return render(request, 'learning_logs/index.html')
