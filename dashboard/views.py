from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


from dashboard.forms import TaskForm, WorkerForm, ProjectForm, WorkerCreateForm
from dashboard.models import Task, Worker, Project


@login_required
def index(request):
    num_tasks = Task.objects.filter(assignee=request.user).count()
    num_completed_tasks = Task.objects.filter(
        assignee=request.user, is_completed=True
    ).count()
    num_projects = Project.objects.filter(team=request.user).count()

    context = {
        "user_tasks": num_tasks,
        "user_projects": num_projects,
        "num_completed_tasks": num_completed_tasks,
        "today_tasks": Task.objects.filter(
            assignee=request.user, deadline=datetime.now()
        ),
    }

    return render(request, "dashboard/index.html", context=context)


class TaskListView(ListView):
    model = Task
    paginate_by = 10


class TaskDetailView(DetailView):
    model = Task


class MyTaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("my-task-list")


class ProjectTaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("project-detail")

    def get_success_url(self):
        project_id = get_object_or_404(Task, id=self.kwargs["pk"]).project_id
        return reverse_lazy("project-detail", kwargs={"pk": project_id})


@login_required()
def task_delete_in_project(request, pk):
    project_id = get_object_or_404(Task, id=pk).project_id
    get_object_or_404(Task, id=pk).delete()
    return HttpResponseRedirect(
        reverse_lazy(viewname="project-detail", args=[project_id])
    )


@login_required()
def task_delete_in_my_task(request, pk):
    get_object_or_404(Task, id=pk).delete()
    return HttpResponseRedirect(reverse_lazy(viewname="my-task-list"))


@login_required()
def my_task_make_is_done(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy(viewname="my-task-list"))


@login_required()
def project_task_make_is_done(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = True
    task.is_completed = True
    task.save()
    project_id = get_object_or_404(Task, id=pk).project_id
    return HttpResponseRedirect(
        reverse_lazy(viewname="project-detail", args=[project_id])
    )


@login_required
def toggle_assign_to_task(request, pk):
    worker = get_object_or_404(Worker, id=request.user.id)
    worker.task_assignee.add(pk)
    project_id = get_object_or_404(Task, id=pk).project_id
    return HttpResponseRedirect(
        reverse_lazy(viewname="project-detail", args=[project_id])
    )


class ProjectTaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("my-task-list")

    def get_success_url(self):
        return reverse_lazy("project-detail", kwargs={"pk": self.kwargs["pk"]})


class MyTaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("my-task-list")


class MyTaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "dashboard/my_task_list.html"
    context_object_name = "task_list"
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class MyProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "dashboard/my_project_list.html"
    context_object_name = "my_projects_list"

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
    form_class = ProjectForm
    success_url = reverse_lazy("project-list")


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse_lazy("project-detail", kwargs={"pk": self.kwargs["pk"]})


class MyProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("my-project-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(project_id=self.kwargs["pk"])
        context["tasks"] = tasks
        return context


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = "projects_list"
    paginate_by = 10


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    paginate_by = 10


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    model = Worker
    form_class = WorkerForm


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Worker
    success_url = reverse_lazy("worker-list")


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    form_class = WorkerCreateForm
    success_url = reverse_lazy("worker-list")
