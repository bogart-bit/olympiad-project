from django.shortcuts import render
from .models import Task, Formula

def tasks_list(request):
    selected_year = request.GET.get('year')
    selected_grade = request.GET.get('grade')

    tasks = Task.objects.all()

    if selected_year and selected_year != 'all':
        try:
            tasks = tasks.filter(year=int(selected_year))
        except ValueError:
            pass

    if selected_grade and selected_grade != 'all':
        tasks = tasks.filter(grade=selected_grade)

    years = Task.objects.values_list('year', flat=True).distinct().order_by('year')
    grades = Task.objects.values_list('grade', flat=True).distinct().order_by('grade')

    if selected_year and selected_year != 'all' and selected_grade and selected_grade != 'all':
        formulas = Formula.objects.filter(year=int(selected_year), grade=selected_grade)
    else:
        formulas = Formula.objects.none()

    context = {
        'tasks': tasks,
        'years': years,
        'grades': grades,
        'selected_year': selected_year,
        'selected_grade': selected_grade,
        'formulas': formulas,
    }
    return render(request, 'tasks.html', context)
def index(request):
    return render(request, 'tasks/index.html')
