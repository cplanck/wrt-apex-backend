from django.contrib import admin
from api.models import *


class APEX_admin(admin.ModelAdmin):
    list_display = ('name','build_date','version')

class APEX_VERSION_admin(admin.ModelAdmin):
    list_display = ('name','details')

class APEX_DEPLOYMENT_admin(admin.ModelAdmin):
    list_display = ('apex', 'deployment_site','post_data_to_database', 'start_date', 'end_date')  

class APEX_RAW_DATA_admin(admin.ModelAdmin):
    list_display = ('uniqueID','gps_hhmmss', 'latitude', 'longitude', 'deployment')  

class DEPLOYMENT_SITE_admin(admin.ModelAdmin):
    list_display = ('name','directory_name','contact','location','country')  

class APEX_RAW_DATA_FILENAMES_admin(admin.ModelAdmin):
    list_display = ('filename','entries_written', 'added_on')


admin.site.register(APEX, APEX_admin)
admin.site.register(APEX_VERSION, APEX_VERSION_admin)
admin.site.register(APEX_DEPLOYMENT, APEX_DEPLOYMENT_admin)
admin.site.register(APEX_RAW_DATA, APEX_RAW_DATA_admin)
admin.site.register(DEPLOYMENT_SITE, DEPLOYMENT_SITE_admin)
admin.site.register(APEX_RAW_DATA_FILENAMES, APEX_RAW_DATA_FILENAMES_admin)


