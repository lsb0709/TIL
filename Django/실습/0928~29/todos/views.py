from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone


def index(request):
    todos = Todo.objects.all()

    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    if deadline == "":
        deadline == timezone.now()

    Todo.objects.create(
        content=content,
        priority=priority,
        deadline=deadline,
    )

    return redirect("todos:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")


def update(reqeust, pk):
    todo = Todo.objects.get(pk=pk)

    todo.completed = not todo.completed

    todo.save()
    return redirect("todos:index")
