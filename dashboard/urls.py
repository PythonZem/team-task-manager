from django.urls import path
from .views import (
    index,
    TaskDetailView,
    TaskCreateView,
    WorkerCreateView,
    MyProjectListView,
    MyTaskListView,
    WorkerListView,
    ProjectDetailView,
    ProjectCreateView,
    toggle_assign_to_task,
    WorkerUpdateView, WorkerDeleteView
)

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', MyTaskListView.as_view(), name='task-list'),
    path("tasks/<int:pk>", toggle_assign_to_task, name='toggle-assign-to-task'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('workers/create/', WorkerCreateView.as_view(), name='worker-create'),
    path("projects/", MyProjectListView.as_view(), name='project-list'),
    path("projects/create", ProjectCreateView.as_view(), name='project-create'),
    path("projects/<int:pk>", ProjectDetailView.as_view(), name="project-detail"),
    path("workers/", WorkerListView.as_view(), name='worker-list'),
    path("workers/update/<int:pk>", WorkerUpdateView.as_view(), name='worker-update'),
    path("workers/delete/<int:pk>", WorkerDeleteView.as_view(), name='worker-delete')
]
