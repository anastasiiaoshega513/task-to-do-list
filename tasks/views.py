from django.shortcuts import render
from django.views import generic

from tasks.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "task_list"
