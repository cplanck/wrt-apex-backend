from django.db import models

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

class APEX_DEPLOYMENT(models.Model):
    apex = models.ForeignKey(APEX, on_delete=models.CASCADE, related_name = 'apex', null=True, blank=True)
    location = models.CharField(max_length = 200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'APEX Deployment'
        verbose_name_plural = 'APEX Deployments'
    
    def __str__(self):
        return str(self.location)

