from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render

tasks= ["foo", "bar", "baz"]
# Create your views here.

class NewTaskform(forms.form):
    task = form.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", min_value=2, max_value=25) #client side validation which will django take care off

def index(request):
    if "tasks" not in request.session: #by session django will identify user
        request.session["tasks"] = []
    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":  #server side validation of form
            form = NewTaskform(request.Post)
            if form.is_valid():
                task = form.cleaned_data["task"] #we are going to take a data from form save it to variable task and then append it with existing task
                #tasks.append(task)
                request.session["tasks"] += [task] #append task
                return HttpResponseRedirect(reverse("tasks:index")) #after submitting the task user will be redirected to tasks page
            else: 
                return render(request, "task/add.html", {
                    "form": form  #if form is not valid then send back it to client again with existing values
                })
        


    return render(request, "tasks.add.html",{
        "form" : NewTaskform
    }
    )

