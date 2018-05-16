from django import forms
from connections.models import ConnectionTable
from accounts.models import FarmUser


class RequestConnection(forms.ModelForm):

    class Meta:
        model = ConnectionTable
        fields = ['user','message_type','direction','client']

    def __init__(self, user, *args, **kwargs):
        super(RequestConnection, self).__init__(*args, **kwargs)
        self.fields['user'] = forms.ModelChoiceField(
            label='User',
            queryset=FarmUser.objects.filter(email=user),
            required=True,
            empty_label=None)



class ApproveConnection(forms.ModelForm):

    class Meta:
        model = ConnectionTable
        fields = ['status']