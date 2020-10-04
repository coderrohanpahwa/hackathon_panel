from django.contrib import admin

# Register your models here.
from .models import Contact,Scoreboard,Answer
admin.site.register(Contact)
admin.site.register(Scoreboard)
admin.site.register(Answer)