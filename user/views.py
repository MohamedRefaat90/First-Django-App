from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as logoutUser
from .form import SignupForm
# Create your views here.

def signup(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    
    return render(request, 'signup.html' , {'form': form})


def login(request):
    print("This user : "+ request.user.username)
    return redirect('home')

# def logout(request):
#     logoutUser(request)
#     return redirect('home')

def password_change(request):
    pass