from django.shortcuts import render
from django.views import generic

from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
