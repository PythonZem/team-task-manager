from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from dashboard.forms import TaskForm, ProjectCreateForm, WorkerCreationForm
from dashboard.models import Task, Worker, Project


def index(request):
    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }

    return render(request, "dashboard/index.html", context=context)
