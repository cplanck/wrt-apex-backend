from django.contrib import admin
from api.models import *


class APEX_admin(admin.ModelAdmin):
    list_display = ('name','build_date','version')

class APEX_VERSION_admin(admin.ModelAdmin):
    list_display = ('name','details')

class APEX_DEPLOYMENT_admin(admin.ModelAdmin):
    list_display = ('apex','location', 'start_date', 'end_date')  


admin.site.register(APEX, APEX_admin)
admin.site.register(APEX_VERSION, APEX_VERSION_admin)
admin.site.register(APEX_DEPLOYMENT, APEX_DEPLOYMENT_admin)
