from django.shortcuts import render
from .models import JoinOurTeam
import requests
# Create your views here.

def jointeam(request):
    if request.method == "POST":
        # recaptcha stuff 
        clientkey=request.POST.get('g-recaptcha-response','default')
        secretkey='6LdbcDQjAAAAAFNRRStnvGPDImFq2Ul8pGWYGApO'
        captchaData={
            'secret':secretkey,
            'response':clientkey
        }
        r=requests.post(' https://www.google.com/recaptcha/api/siteverify',data=captchaData)
        r=r.json()

        if r['success']:
            fname=request.POST.get('fname','default')
            lname=request.POST.get('lname','default')
            email=request.POST.get('email','default')
            phone=request.POST.get('phone','default')
            Position=request.POST.get('Position','default')

            en=JoinOurTeam(fname=fname,lname=lname,email=email,phone=phone,Position=Position)
            en.save()
            p={
                'l':  r['success']
                }
            return render(request,'joinourteamapp/jot.html',p)
    return render(request,'joinourteamapp/jot.html')