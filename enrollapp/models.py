from django.db import models

# Create your models here.

class Enroll(models.Model):
    fname=models.CharField(max_length=130)
    lname=models.CharField(max_length=130)
    email=models.CharField(max_length=1300)
    phone=models.CharField(max_length=130)
    grade=models.CharField(max_length=110)
    GuardiansName=models.CharField(max_length=300)
    # Position=models.TextField()
    # date=models.DateField()


    