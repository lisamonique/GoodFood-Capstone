from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase, JsonResponse
import json
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Answer

# Create your views here.


def veggieGameData(request):
    quiz_question = Question.objects.order_by('pub_date')
    quiz_answer = Answer.objects.all()

    context = {
        "message": "Welcome to Vegetable Game",
        "quiz_question": quiz_question,
        "quiz_answer": quiz_answer
    }
    return render(request, 'vegetableGame/game.html', context)

def getQuiz(request):

    form = request.POST

    quiz = Question()
    quiz.veggie_question = form['veggie_question']
    quiz.save()

    return HttpResponseRedirect(reverse('veggieGameData'))
    


