from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from connections.forms import RequestConnection
from connections.models import ConnectionTable
from django.shortcuts import get_object_or_404

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
    if request.method == 'POST':
        form = RequestConnection(request.user, request.POST, instance=data)   #use data from pulled data?
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('/connections/show_table')
    else:
        form = RequestConnection(request.user, instance=data)
    return render(request, 'connections/modify_connection.html', {'form' : form})
