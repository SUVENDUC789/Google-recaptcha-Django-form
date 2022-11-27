from django.shortcuts import render
from .models import Enroll
import requests
# Create your views here.

def form(request):
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
            grade=request.POST.get('grade','default')
            GuardiansName=request.POST.get('GuardiansName','default')

            en=Enroll(fname=fname,lname=lname,email=email,phone=phone,grade=grade,GuardiansName=GuardiansName)
            en.save()
            p={
                'l':  r['success']
                }
            return render(request,'enrollapp/form.html',p)
    return render(request,'enrollapp/form.html')
