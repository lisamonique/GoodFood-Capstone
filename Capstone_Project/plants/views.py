from django.shortcuts import render
# from vegetableGame.models import Question, Answer

# Create your views here.

def index(request):
    context = {
        'message': 'Welcome to GoodFood'
    }
    return render(request, 'plants/index.html', context)

def aboutPage(request):
    context = {
        "message": "GoodFood Mission"
    }
    return render(request, 'plants/about.html', context)
