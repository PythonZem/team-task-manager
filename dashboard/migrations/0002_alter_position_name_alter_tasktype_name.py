# Generated by Django 4.1 on 2024-03-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='tasktype',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
