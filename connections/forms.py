from django import forms
from connections.models import ConnectionTable

class RequestConnection(forms.ModelForm):
    class Meta:
        model = ConnectionTable
        fields = ['message_type','direction','client']