from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from tasks.models import Task, Tag


def task_toggle(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        task.is_done = not task.is_done
        task.save(update_fields=["is_done"])
    return redirect(reverse("tasks:index"))


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
