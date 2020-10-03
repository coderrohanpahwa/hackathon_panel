from django.contrib import admin

# Register your models here.
from .models import Contact,Scoreboard
admin.site.register(Contact)
admin.site.register(Scoreboard)