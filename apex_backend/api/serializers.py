from rest_framework import serializers
from api.models import *

class APEX_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = APEX_DATA
        fields = '__all__'

class APEX_Serializer(serializers.ModelSerializer):
    class Meta:
        model = APEX
        fields = '__all__'