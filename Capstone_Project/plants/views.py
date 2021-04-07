from django.http import response
from django.shortcuts import render
import requests
import json

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
    app_id = 'c48cccb3'
    app_key = '90a279a59b69df078c597025e6a44c35'
    
    if 'ingr' in request.GET:
        ingr = request.GET['ingr']
    else:
        ingr = 'apple'
    # response = requests.get(f"http://api.edamam.com/auto-complete?q=rou&limit=10&app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}")
    response = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?app_id={app_id}&app_key={app_key}&ingr={ingr}")
    food_data = response.json()
    # print(food_data)
    return render(request, 'plants/food_data.html', {
        'parsed': food_data['parsed'],
        'links': food_data['_links'],
        'hints': food_data['hints']
    })

def viewFood(request):
    
    pass