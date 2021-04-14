from django.urls import path
from . import views

app_name = 'quizGame'
urlpatterns = [
    path('', views.index, name='index'),
    path('getQuestion/', views.getQuestion, name='getQuestion'),
    path('getQuiz/', views.getQuiz, name="getQuiz")
]