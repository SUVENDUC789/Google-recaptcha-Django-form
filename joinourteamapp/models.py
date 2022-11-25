from django.db import models

# Create your models here.

class JoinOurTeam(models.Model):
    fname=models.CharField(max_length=130)
    lname=models.CharField(max_length=130)
    email=models.CharField(max_length=1150)
    phone=models.CharField(max_length=100)
    Position=models.TextField()
    # date=models.DateField()
