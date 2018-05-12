from django.shortcuts import render
from connections.models import ClientTable, ConnectionTable
from django.contrib.auth.decorators import login_required

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
def table(request):
    #data = ConnectionTable.objects.all()
    data = request.user.coder.assignments.all()
    args = {'data': data}

    return render(request, 'connections/con_table.html', args)