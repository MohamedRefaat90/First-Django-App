from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Board , Post, Topic # import the model you want to display
from .forms import NewTopicForm, replyForm



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

@login_required
def new_topic(requset,board_id):

    board = get_object_or_404(Board, pk=board_id)
    # user = User.objects.first()  # get the first user for now

    if requset.method == 'POST':
        # take instace from form
        form = NewTopicForm(requset.POST)

        if form.is_valid():
            # This creates a Topic instance but doesn’t save it to the database yet
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = requset.user

            # Saves the Topic instance to the database.
            topic.save()

            # This creates and saves a new Post instance directly in the database.
            post = Post.objects.create(
                # Retrieves the validated message from the form data and assigns it to the Post
                message = form.cleaned_data.get('message'),
                created_by = requset.user,
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

def topic_posts(request, board_id, topic_id):
    # Retrieve the Topic object with the specified board_id and topic_id.
    # If no such object exists, raise an Http404 exception.
    topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
    return render(request, 'topic_posts.html', {'topic': topic})

def reply_topic(request, board_id, topic_id):
    topic = get_object_or_404(Topic,borad__pk = board_id, pk=topic_id)

    if request.method == "POST":
        form = replyForm(request.post)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', board_id=board_id, topic_id=topic_id)
    else:
        form = replyForm()
        return render(request, 'reply_topic.html', {'topic': topic, 'form': form})


def edit_post(request, board_id, topic_id, post_id):
    
    return render(request, 'edit_post.html')