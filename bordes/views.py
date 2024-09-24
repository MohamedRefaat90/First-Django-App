from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Board # import the model you want to display

# Create your views here.

def home(request):
    boarders = Board.objects.all()

    # render the template and pass the context
    return render(request, 'home.html', {'boarders': boarders}) 

def board_topics(request, board_id):

    board = get_object_or_404(Board, pk=board_id)
    return HttpResponse(board.name)