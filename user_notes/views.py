from django.shortcuts import render
from .models import Subject, Note
# from django.urls import url

# Create your views here.
def index(request):
  urls = []
  subjects = Subject.objects.all()
  for subject in subjects:
    urls.append(request.build_absolute_uri() + f"subject/{subject.title}")  
  
  return render(request, "user_notes/index.html", {"urls":urls, "subjects":subjects, "iteration":range(0,len(urls))})

def subject_notes(request, subject):
  subject_ = Subject.objects.filter(title=subject)[0]
  notes = Note.objects.all().filter(subject=subject_.id)
  return render(request, "user_notes/notes.html", {"notes":notes})