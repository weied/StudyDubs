from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("survey", views.survey, name="survey"),
    path("respond", views.getRespond, name="respond"),
    path("results", views.showResults, name="results"),
    path("summary", views.summary, name="summary"),
    path("getsummary", views.getSummary, name="getsummary"),
    path("chart", views.showChart, name="chart")
]
