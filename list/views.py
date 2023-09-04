from .models import List
from django.urls import reverse
from django.shortcuts import loader, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:
        mylist = List.objects.all().values()
        template = loader.get_template('index.html')
        context = {
            'mylist': mylist,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('index')


@login_required
def addlist(request):
    listname = request.POST['listname']
    username = request.user
    list = List(listname=listname, user=username)
    list.save()
    messages.success(request, "New item has been added successfully.")
    return HttpResponseRedirect(reverse('index'))

    
@login_required
def edit(request, id):
    myeditlist = List.objects.get(id=id)
    mylist = List.objects.all().values()
    template = loader.get_template('edit.html')
    context = {
        'myeditlist': myeditlist,
        'mylist': mylist,
    }
    return HttpResponse(template.render(context, request))


@login_required
def editlist(request, id):
    editlistname = request.POST['listname']
    list = List.objects.get(id=id)
    list.listname = editlistname
    list.save()
    messages.success(request, "Item has been edited successfully.")
    return HttpResponseRedirect(reverse('index'))


@login_required
def deletelist(request, id):
    deletelistname = List.objects.get(id=id)
    deletelistname.delete()
    messages.error(request, "Item has been deleted successfully.")
    return HttpResponseRedirect(reverse('index'))