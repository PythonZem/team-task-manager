from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from dashboard.models import Task, Worker, Project


class TaskForm(forms.ModelForm):
    assignee = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Task
        fields = "__all__"


class WorkerForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = Worker


class WorkerCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
        )


class ProjectForm(forms.ModelForm):

    team = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Project
        fields = "__all__"
