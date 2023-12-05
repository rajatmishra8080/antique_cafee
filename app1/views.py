from django.shortcuts import render,redirect
from .models import contact
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        myuser=contact(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message'],
        )
        myuser.save()
        messages.success(request,'your message sent successfully')
        return redirect('/')
    return render(request,'index.html',{"messages":messages})
