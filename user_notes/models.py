from django.db import models

# Create your models here.
class Subject(models.Model):
  title = models.CharField(max_length=50)

  def __str__(self):
    return self.title

class Note(models.Model):
  title = models.CharField(max_length=200, default="New note")
  contents = models.CharField(max_length=2000)
  date = models.DateField()
  time = models.TimeField()
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  def __str__(self):
    return self.title
