from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'security/index.html')
def signup(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            print(fm)
    fm = UserCreationForm()
    return render(request, 'security/signup.html', {"form": fm})

def signin(request):
    return render(request, 'security/signin.html')

def reset_password(request):
    return render(request, 'security/reset_password.html')
