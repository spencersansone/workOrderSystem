from django.contrib import admin
from .models import *

class ClientList(admin.ModelAdmin):
    list_display = ('first_name','last_name','location','room_number','email',)
    ordering = ['last_name']

admin.site.register(Client, ClientList)

class CommonAreaList(admin.ModelAdmin):
    list_display = ('area_name','location',)
    ordering = ['area_name']

admin.site.register(CommonArea, CommonAreaList)

class ClientRequestList(admin.ModelAdmin):
    list_display = ('id','title','client','description','due_date','technician',)
    ordering = ['due_date']

admin.site.register(ClientRequest, ClientRequestList)

class CommonAreaRequestList(admin.ModelAdmin):
    list_display = ('id','common_area','description','due_date','technician',)
    ordering = ['due_date']

admin.site.register(CommonAreaRequest, CommonAreaRequestList)