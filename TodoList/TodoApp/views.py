from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, Task
from .forms import GroupForm, TaskForm
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        group_name = request.POST.get('grouptask')
        task_description = request.POST.get('task')

        # Ensure both fields are filled
        if group_name and task_description:
            group, created = Group.objects.get_or_create(name=group_name)
            Task.objects.create(group=group, description=task_description)
            return redirect('index')  # Reload the page after adding task

    groups = Group.objects.prefetch_related('tasks').all()
    return render(request, 'TodoApp/index.html', {'groups': groups})

def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after saving changes
    else:
        form = TaskForm(instance=task)
    return render(request, 'TodoApp/task_edit.html', {'form': form, 'task': task})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    group = task.group

    task.delete()

    # Delete the group if there are no more tasks
    if not group.tasks.exists():
        group.delete()

    return JsonResponse({'status': 'success'})
