from django.contrib import admin
from .models import ClientModel, DeveloperModel



class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','name','contact','project_info','price','create_time','finished_date','status')
    search_fields = ['name','contact']
    ordering = ['name','price']


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact','my_info','experience_year','finished_work')
    search_fields = ['name','contact','experience_year','finished_work']
    ordering = ['name','experience_year','finished_work']


admin.site.register(ClientModel, ClientAdmin)
admin.site.register(DeveloperModel, DeveloperAdmin)