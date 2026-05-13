from django.shortcuts import render
from .models import Task

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})