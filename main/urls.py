from django.urls import path
from . import views

urlpatterns = [

    # we leve a blank string to say that index will be the main page, the home page
    path("", views.displayTodo),
    path("addtodo",views.addtodo),
    path("checklist/<int:todo_id>", views.checklist),
    # here's the url the delete button is gonna redirect us,
    # and "<int:todo_id>" is gonna be filledup by the argument we passed in the form block of delete button
    #it's like a function where the parameter is a todo_id integer and we provide the argument in the form block of delete button
    path("deletetodo/<int:todo_id>", views.deletetodo),
    
]
