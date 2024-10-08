from django import forms
from django.contrib.auth.models import User
from regapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):
    
    class Meta:
        model = UserProfileInfo
        fields = ('linkedIn_url',)