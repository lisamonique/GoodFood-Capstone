from django.urls import path
from . import views

app_name = 'quizGame'
urlpatterns = [
    path('', views.index, name='index'),
    path('getQuiz', views.getQuiz, name="getQuiz")
]