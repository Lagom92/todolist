from django.shortcuts import render, redirect
from .forms import TodoModelForm
form django.contrib.auth.decorators import login_required

# Create your views here.

def list(request):
def list(request):
    todos = request.user.todo_set()
    return render(request, "todo/list.html")
    
@login_required
def create(request):
    if request.method == "POST":
        form = TodoModelForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("todos:list")
    else:
        form = TodoModelForm()
        return render(request, "todo/create.html", {"form":form})