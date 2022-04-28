from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("subject/<subject>", views.subject_notes, name="subject_notes"),
    path("new_subject", views.new_subject, name="new_subject")
]