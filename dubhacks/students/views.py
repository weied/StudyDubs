from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse(survey))

def survey(request):
    questions = Question.objects.all().order_by('question')
    return render(request, "survey.html", {'questions': questions})

def getRespond(request):
    ans = {}
    ans['gpa'] = request.POST['gpa']
    ans['name'] = request.POST['name']
    questions = Question.objects.all().order_by('question')
    for q in questions:
        ans[q.name] = request.POST[str(q.name)]
    print(ans)
    return HttpResponse('Hello World!')
