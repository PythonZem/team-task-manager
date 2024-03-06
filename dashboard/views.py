from django.shortcuts import render

from dashboard.models import Task, Worker


def index(request):
    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }

    return render(request, "dashboard/index.html", context=context)
