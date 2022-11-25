from django.contrib import admin
from .models import SchoolContact
# Register your models here.

@admin.register(SchoolContact)

class SchoolContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','aboutcourse']
