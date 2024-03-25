from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def appointment(request):
    return render(request, 'appointment.html')

def consultation(request):
    return render(request, 'consultation.html')

def auth(request):
    return render(request, 'auth.html')