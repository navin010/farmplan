from django.shortcuts import render, redirect
from connections.models import ClientTable, ConnectionTable, FarmUser
from django.contrib.auth.decorators import login_required
from connections.forms import RequestConnection

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
        form = RequestConnection(request.POST, instance=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/connections/show_table')
    else:
        form = RequestConnection(instance=request.user)
    return render(request, 'connections/request_connection.html', {'form' : form})
