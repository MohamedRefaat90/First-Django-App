from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        # This links the form to the Topic model.When the form is submitted,
        # it will create or update a Topic instance.
        model = Topic

        # This defines which fields from the Topic model 
        # should be included in the form
        fields = ['subject', 'message']


class replyForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['message',]