from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from connections.forms import RequestConnection, ApproveConnection
from connections.models import ConnectionTable
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from connections.emails import email_modified,email_requested,email_request_response

# Create your views here.

#Home
@login_required
def home(request):
    numbers = [1,2,3,4,5]
    name = "John Doe"
    args = {'myName': name, 'numbers': numbers}

    return render(request, 'connections/home.html', args)


#Requests Table
@login_required
def requests_table(request):
    if request.user.is_client:
        data = ConnectionTable.objects.filter(client=request.user, status="awaiting approval")
        args = {'data': data}
        return render(request, 'connections/client/requests_table.html', args)
    elif request.user.is_admin:
        return HttpResponse('<h1>Page not found</h1>')
    else:
        data = ConnectionTable.objects.filter(user=request.user, status="awaiting approval")
        args = {'data': data}
        return render(request, 'connections/partner/requests_table.html', args)


#Approved Requests Table
@login_required
def approved_table(request):
    if request.user.is_client:
        data = ConnectionTable.objects.filter(client=request.user, status="approved")
        args = {'data': data}
        return render(request, 'connections/client/approved_table.html', args)
    elif request.user.is_admin:
        return HttpResponse('<h1>Page not found</h1>')
    else:
        data = ConnectionTable.objects.filter(user=request.user, status="approved")
        args = {'data': data}
        return render(request, 'connections/partner/approved_table.html', args)

#Rejected Requests Table
@login_required
def rejected_table(request):
    if request.user.is_client:
        data = ConnectionTable.objects.filter(client=request.user, status="rejected")
        args = {'data': data}
        return render(request, 'connections/client/rejected_table.html', args)
    elif request.user.is_admin:
        return HttpResponse('<h1>Page not found</h1>')
    else:
        data = ConnectionTable.objects.filter(user=request.user, status="rejected")
        args = {'data': data}
        return render(request, 'connections/partner/rejected_table.html', args)



@login_required
def request_connection(request):
    if not request.user.is_client and not request.user.is_admin:
        if request.method == 'POST':
            form = RequestConnection(request.user, request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                email_requested(instance)
                return redirect('/connections/requests_table')
        else:
            form = RequestConnection(request.user)
        return render(request, 'connections/request_connection.html', {'form' : form})
    else:
        return HttpResponse('<h1>Page not found</h1>')


@login_required
def modify_connection(request,slug):
    data = get_object_or_404(ConnectionTable, slug=slug)                                         #pull data from db based on unique slug
    if request.user == data.user and data.status == "awaiting approval":                         #make sure other users can't modify data related to current user
        if request.method == 'POST':
            form = RequestConnection(request.user, request.POST, instance=data)                  #use data from pulled data?
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                email_modified(data)
                return redirect('/connections/requests_table')
        else:
            form = RequestConnection(request.user, instance=data)
        return render(request, 'connections/modify_connection.html', {'form' : form})
    else:
        return HttpResponse('<h1>Page not found</h1>')


@login_required
def delete_connection(request,slug):
    data = get_object_or_404(ConnectionTable, slug=slug)                        #pull data from db based on unique slug
    if request.user == data.user and data.status == "awaiting approval":        #current user can delete on awaiting
        data.delete()
        messages.success(request, "Successfully Deleted")
        return redirect('/connections/requests_table')
    elif request.user == data.client and data.status == "approved":
        data.delete()
        messages.success(request, "Successfully Deleted")
        return redirect('/connections/approved_table')
    elif request.user == data.client and data.status == "rejected":
        data.delete()
        messages.success(request, "Successfully Deleted")
        return redirect('/connections/rejected_table')
    else:
        return HttpResponse('<h1>Page not found</h1>')


@login_required
def approve_connection(request,slug):
    data = get_object_or_404(ConnectionTable, slug=slug)                    #pull data from db based on unique slug
    if request.user == data.client:                                         #only client can view data
        if request.method == 'POST':
            form = ApproveConnection(request.POST, instance=data)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                if data.status == "approved":
                    email_request_response(data)
                    return redirect('/connections/approved_table')
                elif data.status == "rejected":
                    email_request_response(data)
                    return redirect('/connections/rejected_table')
                else:
                    return redirect('/connections/requests_table')
        else:
            form = ApproveConnection(instance=data)
        return render(request, 'connections/approve_connection.html', {'form' : form})
    else:
        return HttpResponse('<h1>Page not found</h1>')