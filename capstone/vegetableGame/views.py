from django.shortcuts import render

# Create your views here.
from .models import Question, Answer

def index(request):
    context = {
        'message': 'Welcome to GoodFood Vegetable Game!'
    }
    return render(request, 'plants/index.html', context)

def veggieGame(request):
    with open('fruitveggieQA.txt', 'r', encoding='utf-8') as file:
        questions = file.read()
    context ={
        "questions": questions
    }

    return render(request, 'vegetableGame/game.html', context)
