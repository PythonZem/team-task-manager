# Generated by Django 4.1 on 2024-03-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0004_remove_task_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]