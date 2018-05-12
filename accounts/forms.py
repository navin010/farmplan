from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import FarmUser, Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    gatekeeper_id = forms.CharField(required=True)
    business_name = forms.CharField(required=True)

    class Meta:
        model = FarmUser
        fields = (
            'email',
            'gatekeeper_id',
            'business_name'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.gatekeeper_id = self.cleaned_data['gatekeeper_id']
        user.business_name = self.cleaned_data['business_name']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = (
            'address',
            'town',
            'county',
            'country',
            'post_code'
        )

