from django.shortcuts import render

def homepage(request):
    context = {}
    return render(request, 'projectapp/homepage.html', context)

def chatbot(request):
    context = {}
    return render(request, 'projectapp/chatbot.html', context)