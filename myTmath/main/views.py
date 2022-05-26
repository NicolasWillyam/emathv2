from cv2 import imreadmulti
from django.shortcuts import render

def home(response):
    return render(response, "main/home.html", {})

def contest(request):
    return render(request, 'main/contest.html')

def task(request):
    return render(request, 'main/task.html')

def problems(request):
    return render(request, 'main/problems.html')

def submissions(request):
    return render(request, 'main/submissions.html')

def login(request):
    return render(request, 'main/login.html')

def class_list(request):
    return render(request, 'main/class_list.html')
