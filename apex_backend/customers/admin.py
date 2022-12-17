from django.contrib import admin
from customers.models import CUSTOMER

class CUSTOMER_admin(admin.ModelAdmin):
    customer = ('user','name')


admin.site.register(CUSTOMER, CUSTOMER_admin)
