from django.urls import path
from .views import (
    index,
    WorkerCreateView,
    MyProjectListView,
    MyTaskListView,
    WorkerListView,
    ProjectDetailView,
    ProjectCreateView,
    toggle_assign_to_task,
    WorkerUpdateView,
    WorkerDeleteView,
    ProjectListView,
    MyProjectDeleteView,
    MyTaskCreateView,
    task_delete_in_my_task,
    task_delete_in_project,
    my_task_make_is_done,
    ProjectUpdateView,
    MyTaskUpdateView,
    ProjectTaskUpdateView,
    TaskDetailView,
    project_task_make_is_done,
    ProjectTaskCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("my-tasks/", MyTaskListView.as_view(), name="my-task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("my-projects/", MyProjectListView.as_view(), name="my-project-list"),
    path("tasks-assign/<int:pk>", toggle_assign_to_task, name="toggle-assign-to-task"),
    path("my-tasks/create/", MyTaskCreateView.as_view(), name="my-task-create"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("projects/create", ProjectCreateView.as_view(), name="project-create"),
    path("projects/<int:pk>", ProjectDetailView.as_view(), name="project-detail"),
    path(
        "projects/update/<int:pk>", ProjectUpdateView.as_view(), name="project-update"
    ),
    path(
        "my-projects/delete/<int:pk>",
        MyProjectDeleteView.as_view(),
        name="my-project-delete",
    ),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/update/<int:pk>", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/delete/<int:pk>", WorkerDeleteView.as_view(), name="worker-delete"),
    path(
        "tasks/delete/<int:pk>", task_delete_in_project, name="task-delete-in-project"
    ),
    path(
        "my-tasks/delete/<int:pk>", task_delete_in_my_task, name="task-delete-my-tasks"
    ),
    path("my-tasks/make-dane/<int:pk>", my_task_make_is_done, name="my-task-make-done"),
    path("my-tasks/update/<int:pk>", MyTaskUpdateView.as_view(), name="my-task-update"),
    path(
        "poject-tasks/update/<int:pk>",
        ProjectTaskUpdateView.as_view(),
        name="project-task-update",
    ),
    path(
        "project-tasks/done/<int:pk>",
        project_task_make_is_done,
        name="project-task-make-done",
    ),
    path(
        "project-tasks/create/<int:pk>",
        ProjectTaskCreateView.as_view(),
        name="project-task-create",
    ),
]
