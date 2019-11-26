from django.shortcuts import render, redirect
from .models import list
from todo.form import *
from django.contrib import messages

# Create your views here.


def todo(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = list.objects.all()
            messages.success(request,('Item has been added to List'))
            return render(request,"user/todo.html",{'all_items': all_items})

    else:
        all_items = list.objects.all()
        return render(request,"user/todo.html",{'all_items':all_items})


def todo_add(request):
    return render(request, "user/todo_add.html",{})


def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item has been Deleted'))
    return redirect('todo')

def cross_off(request,list_id):
    item = list.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo')

def uncross(request,list_id):
    item = list.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo')
