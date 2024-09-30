from django.shortcuts import render
from regapp.models import UserProfileInfo
from regapp import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def userlogin(request):
    pass


def userlogout(request):
    pass


def registration(request):
    registered = False
    
    if request.method == "POST":
        userform = forms.UserForm(data=request.POST)
        profileform = forms.UserProfileInfoForm(data=request.POST)

        if userform.is_valid() and profileform.is_valid():
            userform.save(commit=True)
            profileform.save(commit=True)
            
            registered = True
    else:
        userform = forms.UserForm()
        profileform = forms.UserProfileInfoForm()
        
        
            
    return render(request, 'register.html', {'userform': userform, 'profileform': profileform, 'registered': registered})


    