from django.db import models

# Create your models here.

class SchoolContact(models.Model):
    name=models.CharField(max_length=130)
    email=models.CharField(max_length=1150)
    phone=models.CharField(max_length=100)
    aboutcourse=models.TextField()
    # date=models.DateField()
