from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "message": "Garden Plot Game"
    }
    return render(request, 'gardenPlot/index.html', context)