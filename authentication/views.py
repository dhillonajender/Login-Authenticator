from django.shortcuts import render, redirect
# for mysql without orm
#from django.db import connection
from .models import Usertable


# Create your views here.
def auth(request):
    # request.GET is a dictionary
    usr=request.GET.get('username')
    psd=request.GET.get('pwd')
    users=Usertable.objects.all()
    
    for user in users:
        if(user.username == usr and user.password== psd):
            return redirect('/app/')  
    return render(request, 'login.html', {})
    

def app_interface(request):
    return render(request, 'app-interface.html', {})
