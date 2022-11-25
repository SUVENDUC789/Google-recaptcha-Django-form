from django.shortcuts import render
from .models import SchoolContact
# Create your views here.


def schcontact(request):
    if request.method == "POST":
        name=request.POST.get('name','default')
        email=request.POST.get('email','default')
        phone=request.POST.get('phone','default')
        about=request.POST.get('about','default')

        en=SchoolContact(name=name,email=email,phone=phone,aboutcourse=about)
        en.save()

        
    return render(request,'schcontactapp/schcontact.html')
