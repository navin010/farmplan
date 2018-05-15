from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from connections.forms import RequestConnection
from connections.models import ConnectionTable
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

#Home
@login_required
def home(request):
    numbers = [1,2,3,4,5]
    name = "John Doe"
    args = {'myName': name, 'numbers': numbers}

    return render(request, 'connections/home.html', args)


#Connection Table
@login_required
def show_table(request):
    #data = ConnectionTable.objects.all()
    data = ConnectionTable.objects.filter(user=request.user)
    args = {'data': data}

    return render(request, 'connections/show_table.html', args)


@login_required
def request_connection(request):
    if request.method == 'POST':
        form = RequestConnection(request.user, request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/connections/show_table')
    else:
        form = RequestConnection(request.user)
    return render(request, 'connections/request_connection.html', {'form' : form})


@login_required
def modify_connection(request,slug):
    data = get_object_or_404(ConnectionTable, slug=slug)  #pull data from db based on unique slug
    if request.user == data.user:                         #make sure other users can't modify data related to current user
        if request.method == 'POST':
            form = RequestConnection(request.user, request.POST, instance=data)   #use data from pulled data?
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect('/connections/show_table')
        else:
            form = RequestConnection(request.user, instance=data)
        return render(request, 'connections/modify_connection.html', {'form' : form})
    else:
        return HttpResponse('<h1>Page not found</h1>')


@login_required
def delete_connection(request,slug):
    data = get_object_or_404(ConnectionTable, slug=slug)  #pull data from db based on unique slug
    if request.user == data.user:
        data.delete()
        messages.success(request, "Successfully Deleted")
        return redirect('/connections/show_table')
    else:
        return HttpResponse('<h1>Page not found</h1>')


@login_required
def approve_connection(request,slug):
    data = get_object_or_404(ConnectionTable, slug=slug)    #pull data from db based on unique slug
    if request.user == data.client:                         #only client can view data
        if request.method == 'POST':
            form = RequestConnection(request.user, request.POST, instance=data)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect('/connections/show_table')
        else:
            form = RequestConnection(request.user, instance=data)
        return render(request, 'connections/approve_connection.html', {'form' : form})
    else:
        return HttpResponse('<h1>Page not found</h1>')