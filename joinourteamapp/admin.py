from django.contrib import admin
from .models import JoinOurTeam
# Register your models here.

@admin.register(JoinOurTeam)

class JoinOurTeamAdmin(admin.ModelAdmin):
    list_display=['id','fname','lname','email','phone','Position']
