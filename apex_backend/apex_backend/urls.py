from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = "APEX Dashboard"
admin.site.site_title = "White River Technologies APEX Dashboard"
admin.site.index_title = "Welcome to the White River Technologies APEX Dashboard"
