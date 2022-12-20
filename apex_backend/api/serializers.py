from rest_framework import serializers
from api.models import *

class APEX_RAW_DATA_Serializer(serializers.ModelSerializer):
    class Meta:
        model = APEX_RAW_DATA
        fields = '__all__'

class APEX_Serializer(serializers.ModelSerializer):
    class Meta:
        model = APEX
        fields = '__all__'

class APEX_RAW_DATA_FILENAMES_Serializer(serializers.ModelSerializer):
    class Meta:
        model = APEX_RAW_DATA_FILENAMES
        fields = '__all__'

class APEX_DEPLOYMENT_Serializer(serializers.ModelSerializer):
    
    deployment_site = serializers.CharField(source='deployment_site.name')
    apex = serializers.CharField(source='apex.name')

    class Meta:
        model = APEX_DEPLOYMENT
        fields = ['id', 'apex' ,'status' ,'start_date', 'end_date', 'deployment_site']