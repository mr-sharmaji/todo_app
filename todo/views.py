from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
#from .models import todoItem
# Create your views here
from django.shortcuts import render,redirect
from .models import TodoList, Category
from django.utils import timezone
import time
import datetime
from django.contrib import messages
def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            if str(request.POST["date"]) >=  timezone.now().strftime("%Y-%m-%d"):
                title = request.POST["description"] #title
                date = str(request.POST["date"]) #date
                category = request.POST["category_select"] #category
                content = title + " -- " + date + " " + category #content
                Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
                Todo.save() #saving the todo
                return redirect("/") #reloading the page
            else:
                messages.add_message(request, messages.INFO, 'Invalid Date!')

        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
    return render(request, "index.html", {"todos": todos, "categories":categories})
    # else:
    #     return HttpResponse(request.method)
