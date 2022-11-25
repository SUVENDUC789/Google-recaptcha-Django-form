from django.shortcuts import render
from .models import JoinOurTeam
# Create your views here.

def jointeam(request):
    if request.method == "POST":
        fname=request.POST.get('fname','default')
        lname=request.POST.get('lname','default')
        email=request.POST.get('email','default')
        phone=request.POST.get('phone','default')
        Position=request.POST.get('Position','default')

        en=JoinOurTeam(fname=fname,lname=lname,email=email,phone=phone,Position=Position)
        en.save()
    return render(request,'joinourteamapp/jot.html')