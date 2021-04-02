from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'message': 'Welcome to Flashcard Quiz Game'
    }
    return render(request, 'quizGame/index.html', context)