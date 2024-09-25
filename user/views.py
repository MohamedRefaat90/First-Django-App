from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .form import SignupForm
# Create your views here.

def signup(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            redirect('home')
    
    return render(request, 'signup.html' , {'form': form})