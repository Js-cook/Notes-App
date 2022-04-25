from django.shortcuts import render
from .models import Subject, Note
# from django.urls import url

# Create your views here.
def index(request):
  urls = []
  subjects = Subject.objects.all()
  for subject in subjects:
    urls.append(request.build_absolute_uri() + subject.title)
  
  return render(request, "user_notes/index.html", {"urls":urls})

def subject_notes(request, subject):
  pass