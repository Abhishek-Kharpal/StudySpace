from django.shortcuts import render
from .models import Subject
from django.views.generic import(
    ListView
)
# Create your views here.

class SubjectListView(ListView):
    model=Subject
    template_name='space/index.html'
    context_object_name='subjects'