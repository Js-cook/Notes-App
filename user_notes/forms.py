from django import forms
from .models import Subject

class SubjectForm(forms.Form):
  title = forms.CharField(label="Title", max_length=50)

class NoteForm(forms.Form):
  title = forms.CharField()
  contents = forms.CharField()
  subject = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())