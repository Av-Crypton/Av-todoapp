from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by('time')
    form = TaskForm()
    
    return render(request, 'index.html', {'form': form, 'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
        else:
            pass
    else:
        form = TaskForm(None)
    return redirect('/')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')