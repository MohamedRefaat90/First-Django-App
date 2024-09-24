from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from .models import Board , Post # import the model you want to display
from .forms import NewTopicForm



# Create your views here.

def home(request):
    boarders = Board.objects.all()

    # render the template and pass the context
    return render(request, 'home.html', {'boarders': boarders}) 

def board_topics(request, board_id):

    # get_object_or_404(Board, pk=board_id): This retrieves the Board object
    # from the database using the provided board_id.
    # If the board doesn't exist, Django will return a 404 (Not Found) error.
    # This ensures that the function only continues if the board is valid.
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html', {'board': board})

def new_topic(requset,board_id):
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.first()  # get the first user for now

    if requset.method == 'POST':
        # take instace from form
        form = NewTopicForm(requset.POST)

        if form.is_valid():
            # This creates a Topic instance but doesn’t save it to the database yet
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user

            # Saves the Topic instance to the database.
            topic.save()

            # This creates and saves a new Post instance directly in the database.
            post = Post.objects.create(
                # Retrieves the validated message from the form data and assigns it to the Post
                message = form.cleaned_data.get('message'),
                created_by = user,
                Topic = topic

            )
            # TODO: redirect to the created topic page
            print('redirect to the created topic page')
            return redirect('board_topics', board_id=board.pk)  
    else:
        # If the request method is not POST,
        # an empty NewTopicForm is instantiated and displayed to the user.
        print('redirect to the new_topic page')
        form = NewTopicForm()

    return render(requset,'new_topic.html',{'board':board,'form':form})    