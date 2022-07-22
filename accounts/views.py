from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request, 'accounts/signup.html')

def signin(request):
    return render(request, 'accounts/signin.html')

def profile(request):
    return render(request, 'accounts/profile.html')