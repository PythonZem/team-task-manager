from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=40)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class TaskType(models.Model):
    name = models.CharField(max_length=30)


class Task(models.Model):
    CHOICES = (
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
        (4, "Urgent"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    deadline = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, choices=CHOICES)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignee = models.ManyToManyField(Worker, related_name="workers")
