from django.shortcuts import render
from .models import SchoolContact
import requests
# Create your views here.


def schcontact(request):
    if request.method == "POST":
        clientkey=request.POST.get('g-recaptcha-response','default')
        secretkey='6LdbcDQjAAAAAFNRRStnvGPDImFq2Ul8pGWYGApO'
        captchaData={
            'secret':secretkey,
            'response':clientkey
        }
        r=requests.post(' https://www.google.com/recaptcha/api/siteverify',data=captchaData)
        r=r.json()

        if r['success']:
            name=request.POST.get('name','default')
            email=request.POST.get('email','default')
            phone=request.POST.get('phone','default')
            about=request.POST.get('about','default')

            en=SchoolContact(name=name,email=email,phone=phone,aboutcourse=about)
            en.save()
            p={
                'l':  r['success']
            }
            return render(request,'schcontactapp/schcontact.html',p)
        
    return render(request,'schcontactapp/schcontact.html')
