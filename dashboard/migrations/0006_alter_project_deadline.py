# Generated by Django 4.1 on 2024-03-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_project_description_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(auto_now_add=True),
        ),
    ]
