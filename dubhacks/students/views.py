from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

import datetime

from .models import *
# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse(survey))

def survey(request):
    #questions = Question.objects.all().order_by('question')
    return render(request, "survey0.html")

def getRespond(request):
    answer = Answer(name=request.POST['name'], gpa=request.POST['gpa'],
                    visual=request.POST['visual'], auditory=request.POST['auditory'],
                    kinect=request.POST['kinect'])
    answer.save()
    return HttpResponse('Success!')

def summary(request):
    return render(request, "summary.html")

def getSummary(request):
    date = datetime.datetime.now()
    rating = request.POST['rating']
    text = request.POST['summary']
    summary = Summary(date=date, rating=rating, comment=text)
    summary.save()
    return HttpResponseRedirect(reverse(chart))

def showResults(request):
    names = ["Scott STEWART", "Emily THOMPSON", "Michelle HILL", "Benjamin CLARK"]
    return render(request, "results.html", {"names": names})

def showChart(request):
    return render(request, "chart.html")
