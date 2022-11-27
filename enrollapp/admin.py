from django.contrib import admin
from .models import Enroll
# Register your models here.

@admin.register(Enroll)

class EnrollAdmin(admin.ModelAdmin):
    list_display=['id','fname','lname','email','phone','grade','GuardiansName']
