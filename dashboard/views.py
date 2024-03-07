from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from dashboard.forms import TaskForm, ProjectCreateForm, WorkerCreationForm
from dashboard.models import Task, Worker, Project


@login_required
def index(request):
    num_tasks = Task.objects.filter(assignee=request.user).count()
    num_projects = Project.objects.filter(team=request.user).count()

    context = {
        "user_tasks": num_tasks,
        "user_projects": num_projects,
    }

    return render(request, "dashboard/index.html", context=context)
