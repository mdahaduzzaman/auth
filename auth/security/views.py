from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'security/index.html')
def signup(request):
    return render(request, 'security/signup.html')

def signin(request):
    return render(request, 'security/signin.html')

def reset_password(request):
    return render(request, 'security/reset_password.html')
