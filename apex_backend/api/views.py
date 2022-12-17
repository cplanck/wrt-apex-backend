from django.shortcuts import render
from api.serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from api.models import *


class APEX_Data(viewsets.ModelViewSet):

	""" viewset for returning APEX data """

	# permission_classes = [permissions.IsAuthenticated]
	serializer_class = APEX_Data_Serializer
	queryset = APEX_DATA.objects.all()


class APEX(viewsets.ModelViewSet):

	""" viewset for returning APEX metadata """

	# permission_classes = [permissions.IsAuthenticated]
	serializer_class = APEX_Serializer
	queryset = APEX.objects.all()
