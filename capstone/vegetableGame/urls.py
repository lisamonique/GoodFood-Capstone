
from django.urls import path
from . import views

app_name = 'vegetableGame'
urlpatterns = [
    path('', views.index, name='index'),
    path('veggieGame/', views.veggieGame, name='veggieGame')
]