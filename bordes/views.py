from django.shortcuts import render
from django.http import HttpResponse

from .models import Board # import the model you want to display

# Create your views here.

def home(request):
    borders = Board.objects.all()

    # render the template and pass the context
    return render(request, 'home.html', {'borders': borders}) 