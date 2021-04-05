from django.http import response
from django.shortcuts import render
import requests
import json

# from vegetableGame.models import Question, Answer

# Create your views here.

def index(request):
    context = {
        'message': 'Welcome to GoodFood RealFood'
    }
    return render(request, 'plants/index.html', context)

def aboutPage(request):
    context = {
        "message": "GoodFood Mission"
    }
    return render(request, 'plants/about.html', context)

def edamam(request):
    pass
    # response = requests.get('https://api.edamam.com/api/food-database/v2/parser?')
    # if 'ingr' in request.GET:
    #     ingr = request.GET['ingr']
    # food_data = response.json()
    # return render(request, 'plants/food_data.html', {
    #     # 'food': food_data['food']['parsed'],
    #     'parsed': food_data['parsed']['food'],
    #     '_links': food_data['_links'], 
    #     'ingr': ingr,
    #     'app_id' : 'c48cccb3',
    #     'app_key': '90a279a59b69df078c597025e6a44c35'
    return render(request, 'plants/about.html')