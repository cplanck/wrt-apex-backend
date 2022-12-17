from django.db import models
from django.contrib.auth.models import User

class CUSTOMER(models.Model):
    
    contact = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return str(self.name)