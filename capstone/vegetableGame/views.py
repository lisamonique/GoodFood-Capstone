from django.http.response import JsonResponse
import json
from django.shortcuts import render
from .models import Question, Answer

# Create your views here.


def veggieGameData(request):
    with open('fruitveggie.json', 'r') as file:
        raw_text = file.read()
    database = json.loads(raw_text)

    context = {
        "database": database
    }
    return render(request, 'vegetableGame/game.html', context)

def getQuiz(request):
    quizzes = Question.objects.all()
    
    response = {'data': []}
    for quiz in quizzes:
        response['data'].append({
            'veggie_question': quiz.question
        })
    return JsonResponse(response)

