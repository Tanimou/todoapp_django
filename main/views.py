from audioop import add
from django.shortcuts import render
from .models import Todo
from django.views.decorators.csrf import csrf_exempt#we need to import this to bypass csrf protection
from django.utils import timezone
from django.http import HttpResponseRedirect




#we put this decorator to bypass the csrf protection on this function
@csrf_exempt
def addtodo(request):
    #the output will be a dictionnary
    #print(request.POST)
    current_date=timezone.now()
    #here we grap the content of the input define in index.html
    content=request.POST.get("content")
    checked=request.POST.get("checks[]")
    #we need to create the todo object
    #this object will be added directly in the database 
    # because of Post method defined in the form block in index.html
    Todo.objects.create(added_date=current_date,text=content)
    return HttpResponseRedirect("/")#redirect to the home page. "/" means the home page whic is defined in the url.py



#here "todo_id" is the name of the parameter we defined in urls.py


def displayTodo(request):
    todo_items=Todo.objects.all().order_by("-added_date")#"-" means to take objects from the newest to the older. 
                                                         #instead of the older to the newest
                                                         #it's kinda reverse the list of todo_items
                                              
    #therefore we can return an added_date-ordered dictionary from the newest to older
    return render(request,"index.html",{"todo_items":todo_items})


@csrf_exempt
def checklist(request,todo_id):
    
   #² if request.method=="POST":
    #checked=request.POST.get("checks")
    
    dd=Todo.objects.get(id=todo_id)
    if dd.is_check:
     Todo.objects.filter(id=todo_id  # int(checked)
                            ).update(is_check=False)
    else:
         Todo.objects.filter(id=todo_id  # int(checked)
                            ).update(is_check=True)
   
    return HttpResponseRedirect("/")


@csrf_exempt
def deletetodo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")