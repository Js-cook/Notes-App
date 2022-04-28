from django.shortcuts import render, redirect
from .models import Subject, Note
from .forms import SubjectForm, NoteForm

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

def new_subject(request):
  if request.method == "POST":
    form = SubjectForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect("index")
  else:
    form = SubjectForm()
  return render(request, "user_notes/subject_create.html", {"form":form})  
  