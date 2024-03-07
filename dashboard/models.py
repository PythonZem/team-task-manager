from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"


class TaskType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    deadline = models.DateTimeField(auto_now_add=True)
    team = models.ManyToManyField(Worker, related_name="projects")

    def __str__(self):
        return self.name


class Task(models.Model):
    CHOICES_PRIORITY = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Urgent", "Urgent"),
    )
    CHOICES_STATUS = (
        ("TO DO", "TO DO"),
        ("IN PROGRESS", "IN PROGRESS"),
        ("DONE", "DONE"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, choices=CHOICES_PRIORITY)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignee = models.ManyToManyField(Worker, related_name="task_assignee")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
