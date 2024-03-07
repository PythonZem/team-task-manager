from django.contrib import admin

from dashboard.models import (
    Worker,
    Task,
    TaskType,
    Position,
    Project
)


admin.site.register(Worker)
admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(Position)
admin.site.register(Project)
