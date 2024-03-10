from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db import models


class Position(PermissionsMixin):
    name = models.CharField(max_length=40, unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        related_name="position_set",
        related_query_name="position",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("position permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="position_set",
        related_query_name="position",
    )

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"


class TaskType(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
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

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, choices=CHOICES_PRIORITY)
    task_type = models.ForeignKey(
        TaskType, on_delete=models.CASCADE, blank=True, null=True
    )
    assignee = models.ManyToManyField(Worker, related_name="task_assignee")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
