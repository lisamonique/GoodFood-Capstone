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

    context = {
        'message': 'Welcome to Flashcard Quiz Game',
        "quiz_question": quiz_question,
        "quiz_answer": quiz_answer
    }
    return render(request, 'quizGame/index.html', context)

def getQuiz(request):

    form = request.POST

    quiz = Question()
    quiz.veggie_question = form['veggie_question']
    quiz.save()

    return HttpResponseRedirect(reverse('quizGame'))

def getQuestion(request):
    quiz_question = Question.objects.all()
    response = {'data': []}
    for mon in quiz_question:
        response['data'].append({
            'veggie_question': mon.veggie_question
        })
    return JsonResponse(response)