from django.http import response, JsonResponse
from django.shortcuts import render
import requests
import json

# Create your views here.

def index(request):
    context = {
        'message': 'GARDEN LIGHT'
    }
    return render(request, 'plants/index.html', context)

def aboutPage(request):
    context = {
        "message": "GARDEN LIGHT"
    }
    return render(request, 'plants/about.html', context)

def foodData(request):
    context = {
        "message": 'GARDEN LIGHT'
    }
    return render(request, 'plants/food_data.html', context)

def dashboard(request):
    context = {
        'message': "GARDEN LIGHT"
    }
    return render(request, 'plants/dashboard.html', context)

def edamam(request):
    app_id = 'c48cccb3'
    app_key = '90a279a59b69df078c597025e6a44c35'
    
    if 'ingr' in request.GET:
        ingr = request.GET['ingr']
    else:
        ingr = 'apple'
    response = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?app_id={app_id}&app_key={app_key}&ingr={ingr}")
    food_data = response.json()
    # print(food_data)
    return JsonResponse(food_data)

def viewRecipe(request):
    app_id = '93d4089b'
    app_key = '6ea9ab5bdd103f1738c335f4f163e3b1'
    if 'q' in request.GET:
        query = request.GET['q']
    else:
        query = 'chicken'
    response = requests.get(f"https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}")
    recipe_data = response.json()
    # print(recipe_data)
    return JsonResponse(recipe_data)