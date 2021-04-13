from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    if request.method == "GET":
        error = request.GET.get('error', '')

    context = {
        "message": "Garden Plot Game",
        'error': error
    }
    
    if request.user.is_authenticated:
        return render(request, 'gardenPlot/index.html', context)
    else:
        return HttpResponseRedirect(reverse('plants:index') + '?error=You Are Not Logged In!')
