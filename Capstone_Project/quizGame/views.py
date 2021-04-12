from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase, JsonResponse
import json
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Answer

# Create your views here.


def index(request):
    quiz_question = Question.objects.all()
    quiz_answer = Answer.objects.all()
    
    if request.method == "GET":
        error = request.GET.get('error', '')

    context = {
        'message': 'Welcome to Flashcard Quiz Game',
        "quiz_question": quiz_question,
        "quiz_answer": quiz_answer,
        'error': error
    }
    if request.user.is_authenticated:
        return render(request, 'quizGame/index.html', context)
    else:
        return HttpResponseRedirect(reverse('plants:index') + '?error=You Are Not Logged In!')

def getQuiz(request):

    with open('fruitveggie.json', 'r') as file:
            data = file.read()

    veggie_data = json.loads(data)
    # Question.objects.all().delete()
    # Answer.objects.all().delete()
    print(veggie_data)

    for info in veggie_data:
        food = Question()
        food.veggie_question = info['veggie_question']
        food.save()
        db_types = []
        for answer in info['answers']:
            obj, created = Answer.objects.get_or_create(veggie_answer=answer, question=food)
            db_types.append(obj)
        # print(food)

    return JsonResponse(veggie_data)

def getQuestion(request):
    quiz_question = Question.objects.all()
    response = {'data': []}
    for mon in quiz_question:
        response['data'].append({
            'veggie_question': mon.veggie_question
        })
    return JsonResponse(response)