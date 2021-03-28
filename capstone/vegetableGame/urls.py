from django.urls import path
from . import views

app_name = 'vegetableGame'
urlpatterns = [
    path('veggieGameData/', views.veggieGameData, name='veggieGameData'),
]