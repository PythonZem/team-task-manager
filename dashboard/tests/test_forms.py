from django.test import TestCase
from dashboard.models import Position, Worker, TaskType, Project, Task
from dashboard.forms import TaskForm, WorkerForm, WorkerCreateForm, ProjectForm
from django.contrib.auth import get_user_model


class TaskFormTest(TestCase):
    def test_task_form_valid(self):
        user = get_user_model().objects.create(username='testuser', password='password')
        task_type = TaskType.objects.create(name='Test Task Type')
        project = Project.objects.create(name='Test Project')
        form_data = {
            'name': 'Test Task',
            'description': 'This is a test task',
            'deadline': '2024-03-10',
            'priority': 'High',
            'task_type': task_type.id,
            'project': project.id,
            'assignee': [user.id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())


class WorkerFormTest(TestCase):

    def test_worker_form_valid(self):
        user = get_user_model().objects.create(username='testuser', password='password')
        position = Position.objects.create(name='Test Position')
        form_data = {
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'position': position.id,
        }
        form = WorkerForm(instance=user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_form_invalid(self):
        form = WorkerForm(data={})
        self.assertFalse(form.is_valid())


class WorkerCreateFormTest(TestCase):
    def test_worker_create_form_valid(self):
        form_data = {
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123',
        }
        form = WorkerCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_create_form_invalid(self):
        form = WorkerCreateForm(data={})
        self.assertFalse(form.is_valid())


class ProjectFormTest(TestCase):

    def test_project_form_valid(self):
        form_data = {
            'name': 'Test Project',
            'description': 'This is a test project',
            'deadline': '2024-03-10',
        }
        form = ProjectForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_project_form_invalid(self):
        form = ProjectForm(data={})
        self.assertFalse(form.is_valid())
