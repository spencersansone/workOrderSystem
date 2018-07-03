from django.contrib import admin
from .models import *

class RequestEntryList(admin.ModelAdmin):
    list_display = ('id','due_date','title','technician',)
    ordering = ['due_date']

admin.site.register(RequestEntry, RequestEntryList)