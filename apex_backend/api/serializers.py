from rest_framework import serializers
from django.contrib.auth.models import User
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


class USER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'is_staff', 'last_login', 'date_joined']


class APEX_DEPLOYMENT_Serializer(serializers.ModelSerializer):
    
    deployment_site = serializers.CharField(source='deployment_site.name')
    country = serializers.CharField(source='deployment_site.country')
    city = serializers.CharField(source='deployment_site.city')
    state = serializers.CharField(source='deployment_site.state')
    apex = serializers.CharField(source='apex.name')

    class Meta:
        model = APEX_DEPLOYMENT
        fields = ['id', 'apex' ,'status' ,'start_date', 'end_date', 'deployment_site', 'utm_zone', 'country', 'state', 'city']

class APEX_DECODE_Serializer(serializers.ModelSerializer):
    class Meta:
        model = APEX_DEPLOYMENT
        fields = '__all__'
