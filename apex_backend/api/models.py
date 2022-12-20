from django.db import models
from customers.models import CUSTOMER

class APEX_VERSION(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(blank=True)

    class Meta:
        verbose_name = 'APEX Version'
        verbose_name_plural = 'APEX Versions'

    def __str__(self):
        return str(self.name)

class APEX(models.Model):
    name = models.CharField(max_length=50)
    build_date = models.DateField(null=True, blank=True)
    version = models.ForeignKey(APEX_VERSION, on_delete=models.CASCADE, related_name = 'version', null=True, blank=True)

    class Meta:
        verbose_name = 'APEX'
        verbose_name_plural = 'APEXs'

    def __str__(self):
        return str(self.name)

class DEPLOYMENT_SITE(models.Model):
    name = models.CharField(max_length = 100) 
    directory_name = models.CharField(max_length = 100, default='') 
    contact = models.ForeignKey(CUSTOMER, on_delete=models.CASCADE, related_name = 'apex_deployment', null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name = 'Deployment Site'
        verbose_name_plural = 'Deployment Sites'

    def __str__(self):
        return str(self.name)

class APEX_DEPLOYMENT(models.Model):
    apex = models.ForeignKey(APEX, on_delete=models.CASCADE, related_name = 'apex', null=True, blank=True)
    status = models.BooleanField(default=False)
    deployment_site = models.ForeignKey(DEPLOYMENT_SITE, on_delete=models.CASCADE, related_name = 'deployment_site', null=True, blank=True)
    post_data_to_database = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'APEX Deployment'
        verbose_name_plural = 'APEX Deployments'
    
    def __str__(self):
        return str(self.apex.name) + " Deployment"

class APEX_RAW_DATA(models.Model):
    uniqueID = models.CharField(max_length = 100, unique=True) 
    filename = models.CharField(max_length = 200, default='')
    gps_hhmmss = models.DecimalField(decimal_places=3,max_digits=21, default=0,null=True, blank=True)
    latitude = models.DecimalField(decimal_places=8, max_digits=20,null=True, blank=True)
    longitude = models.DecimalField(decimal_places=8, max_digits=20,null=True, blank=True)
    deployment = models.ForeignKey(APEX_DEPLOYMENT, on_delete=models.CASCADE, related_name = 'apex_deployment', null=True, blank=True)
    
    class Meta:
        verbose_name = 'APEX Raw Data'
        verbose_name_plural = 'APEX Raw Data'

    def __str__(self):
        return str(self.uniqueID)


class APEX_RAW_DATA_FILENAMES(models.Model):
    filename = models.CharField(max_length = 200)
    entries_written = models.IntegerField(null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'APEX Data Filename'
        verbose_name_plural = 'APEX Data Filenames'

    def __str__(self):
        return str(self.filename)

