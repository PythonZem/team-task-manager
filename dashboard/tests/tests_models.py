from django.test import TestCase
from dashboard.models import Position, Worker, TaskType, Project, Task


class PositionModelTest(TestCase):

    def test_string_representation(self):
        position = Position(name="Manager")
        self.assertEqual(str(position), position.name)


class WorkerModelTest(TestCase):

    def test_string_representation(self):
        worker = Worker(first_name="John", last_name="Doe")
        self.assertEqual(str(worker), f"John Doe ({worker.position})")


class TaskTypeModelTest(TestCase):

    def test_string_representation(self):
        task_type = TaskType(name="Bug Fix")
        self.assertEqual(str(task_type), task_type.name)


class ProjectModelTest(TestCase):

    def test_string_representation(self):
        project = Project(name="Project X")
        self.assertEqual(str(project), project.name)


class TaskModelTest(TestCase):

    def test_string_representation(self):
        task = Task(name="Task A")
        self.assertEqual(str(task), task.name)
