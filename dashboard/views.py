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


class TaskListView(ListView):
    model = Task
    paginate_by = 20


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-list")


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("worker-list")


class MyProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "dashboard/my_project_list.html"
    context_object_name = "projects_list"

    def get_queryset(self):
        return Project.objects.filter(team=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(project_id=self.kwargs["pk"])
        context["tasks"] = tasks
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectCreateForm
    success_url = reverse_lazy("project-list")


class MyTaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "dashboard/my_task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)

