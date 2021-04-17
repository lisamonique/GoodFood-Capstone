from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase, JsonResponse
import json
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Answer
import random

# Create your views here.


def index(request):
    if request.method == "GET":
        error = request.GET.get('error', '')

    context = {
        'message': 'Welcome to Flashcard Quiz Game',
        'error': error
    }
    quiz_question = Question.objects.all()
    quiz_answer = Answer.objects.all()

    if request.user.is_authenticated:
        return render(request, 'quizGame/index.html', context)
    else:
        return HttpResponseRedirect(reverse('login_user'))

def getQuiz(request):
    questions = list(Question.objects.all().values())

    response = {'questions': []}
    for question in questions:
        answers = list(Answer.objects.filter(
            question=question['id']).values('veggie_answer'))
        correct_answer = list(Answer.objects.filter(
            question=question['id'], correct=True).values())

        if len(correct_answer) > 0:
            correct_answer = correct_answer[0]['veggie_answer']
        else:
            correct_answer = ''
        response['questions'].append({
            'question': question['veggie_question'],
            'answers': answers,
            'correctAnswer': correct_answer
        })

    return JsonResponse(response, safe=False)


def getQuestion(request):
    quiz_question = Question.objects.all()
    response = {'data': []}
    for mon in quiz_question:
        response['data'].append({
            'veggie_question': mon.veggie_question
        })
    return JsonResponse(response)