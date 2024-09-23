from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.

def home(request):
    borders = Board.objects.all()
    borderList = []
    for border in borders:
        borderList.append(border.name)

    return HttpResponse(borderList)